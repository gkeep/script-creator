import sys


class Constructor:
    # голова скрипта с проверкой на наличие docker
    head = """#!/bin/bash

docker_pfx=""
if [[ -n "$(command -v docker)" ]] && [[ -n "$(docker container ls --format 'table {{.Names}}' 2>/dev/null | grep 'ekd-postgresql')" ]]; then
       docker_pfx="docker exec --user postgres ekd-postgresql"
fi
    """

    # таблицы
    ekd_ca_table = """
ekd_ca=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_ca_'")
"""
    ekd_ekd_table = """
ekd_ekd=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_ekd_'")
"""
    ekd_id_table = """
ekd_id=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_id_'")
"""
    ekd_file_table = """
ekd_file=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_file_[^proc%]'")
"""
    ekd_file_processing_table = """
ekd_file_processing=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_file_processing'")
"""
    ekd_ftp_uploader_table = """
ekd_ftp_uploader=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_ftp_uploader'")
"""
    ekd_notification_table = """
ekd_notification=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_notification'")
"""
    ekd_request_logger_table = """
ekd_request_logger=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_request_logger'")
"""
    ekd_session_table = """
ekd_session=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ~ 'ekd_session'")
"""
    ekd_metadata_table = 'ekd_metadata="ekd_metadata"'
    ekd_repeat_table = 'ekd_repeat_notification="ekd_repeat_notification_db"'
    ekd_calendar_table = 'ekd_calendar="ekd_calendar_db"'
    ekd_chat_table = 'ekd_chat="ekd_chat_db"'
    ekd_showcase_db = 'ekd_showcase="ekd_showcase_db"'

    command = '\n$docker_pfx psql --dbname ${} -c "{}"\n'
    command_with_output = ('\n$docker_pfx psql --dbname ${} -c "COPY(\n{}\n) '
                           'TO STDOUT DELIMITER E\',\' CSV HEADER;" >> {}\n')

    def make_script(self, sql_scripts: dict) -> str:
        """
            tables: используемые таблицы в скрипте
            sql_scripts: словарь таблицы и скрипта к ней, например:
                {"ekd_ca": '<SQL>'}
        """
        out = self.head

        tables = sql_scripts.keys()

        if "ekd_ca" in tables:
            out += self.ekd_ca_table
        if "ekd_ekd" in tables:
            out += self.ekd_ekd_table
        if "ekd_id" in tables:
            out += self.ekd_id_table
        if "ekd_file" in tables:
            out += self.ekd_file_table
        if "ekd_file_processing" in tables:
            out += self.ekd_file_processing_table
        if "ekd_notification" in tables:
            out += self.ekd_notification_table
        if "ekd_request_logger" in tables:
            out += self.ekd_request_logger_table
        if "ekd_session" in tables:
            out += self.ekd_session_table
        if "ekd_metadata" in tables:
            out += self.ekd_metadata_table
        if "ekd_repeat_notification" in tables:
            out += self.ekd_repeat_table
        if "ekd_calendar" in tables:
            out += self.ekd_calendar_table
        if "ekd_chat" in tables:
            out += self.ekd_chat_table
        if "ekd_showcase" in tables:
            out += self.ekd_showcase_db

        for key, value in sql_scripts.items():
            body = ""
            if key not in ("ekd_metadata", "ekd_repeat_notification", "ekd_calendar", "ekd_chat", "ekd_showcase"):
                body += f"SET search_path to public, {key};\n"
            body += value["body"].replace('$', '\\$').replace('"', '\\\"').replace(f"{key}.", '')
            if value["outfile"] != "":
                out += self.command_with_output.format(key, body.replace(';', ''), value["outfile"])
            else:
                out += self.command.format(key, body)

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
