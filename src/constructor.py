import sys


class Constructor:
    # голова скрипта с проверкой на наличие docker
    head = """#!/bin/bash

docker_pfx=""
if [[ -n "$(command -v docker)" ]] && [[ -n "$(docker container ls --format 'table {{.Names}}' 2>/dev/null | grep 'ekd-postgresql')" ]]; then
       docker_pfx="docker exec --user postgres ekd-postgresql"
fi

get_db() {
    local db_name=$1
    if [[ "$db_name" == 'ekd_file' ]]; then
            db_name='ekd_file_[^proc%]'
    fi

    result=$($docker_pfx psql -A -t -c "
    SELECT
        CASE
            WHEN datname ~ '_main' THEN datname
            ELSE (SELECT datname FROM pg_database WHERE datname ~ '_$db_name' LIMIT 1)
        END AS dn
    FROM pg_database
    WHERE (datname ~ '_main' OR datname ~ '_$db_name') AND datname IS NOT NULL LIMIT 1;")

    echo "$result"
}
    """

    ekd_metadata_table = '\nekd_metadata="ekd_metadata"'
    ekd_repeat_table = '\nekd_repeat_notification="ekd_repeat_notification_db"'
    ekd_calendar_table = '\nekd_calendar="ekd_calendar_db"'
    ekd_chat_table = '\nekd_chat="ekd_chat_db"'
    ekd_showcase_db = 'ekd_showcase="ekd_showcase_db"'

    command = '\n$docker_pfx psql --dbname {}{} -c "{}"'

    def make_script(self, sql_scripts: dict) -> str:
        """
            tables: используемые таблицы в скрипте
            sql_scripts: словарь таблицы и скрипта к ней, например:
                {"ekd_ca": '<SQL>'}
        """
        out = self.head

        container_dbs = ("ekd_metadata", "ekd_repeat_notification", "ekd_calendar", "ekd_chat", "ekd_showcase")

        for key, value in sql_scripts.items():
            body = value["body"].replace('$', '\\$').replace('"', '\\\"').replace(f"{key}.", '')

            dbname = f"{key}_db"
            if key not in container_dbs:
                dbname = f"$(get_db '{key}')"

            if dbname == 'ekd_metadata_db':
                dbname = 'ekd_metadata'

            if value["outfile"] != "":
                out += self.command.format(dbname, " -A -t",
                                           (f'SET search_path to public, {key};\n'
                                            f'COPY({body}) TO STDOUT DELIMITER E\',\' CSV HEADER;'))
                out += f' >> {value["outfile"]}'
            else:
                out += self.command.format(dbname, "", f"SET search_path to public, {key};\n{body}")

        return out

    def build_specific(self, db_name: str, filepath: str):
        script = ""
        with open(filepath, 'r') as sql_script:
            for line in sql_script.readlines():
                script += f"{line}"

        bash_script = self.make_script({
            db_name: script.replace('$', '\\$').replace('"', '\\\"')})

        with open(filepath.replace(".sql", ".sh"), 'w') as bash:
            bash.write(bash_script)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        db = sys.argv[1]
        script_path = sys.argv[2]
        cstr = Constructor()

        cstr.build_specific(db, script_path)
        sys.exit()
