class Constructor:
    # голова скрипта с проверкой на наличие docker
    head = """#!/bin/bash

docker_pfx="docker exec --user postgres ekd-postgresql"
if [[ -n "$(command -v docker)" ]] && [[ -n "$(docker container ls --format 'table {{.Names}}' 2>/dev/null | grep 'ekd-postgresql')" ]]; then
       docker_pfx=""
fi
    """

    # таблицы
    ekd_ca_table = """
ekd_ca=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_ca%'")
"""
    ekd_ekd_table = """
ekd_ekd=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_ekd_%'")
"""
    ekd_id_table = """
ekd_id=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_id_%'")
"""
    ekd_file_table = """
ekd_file=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_file_%'")
"""
    ekd_file_processing_table = """
ekd_file_processing=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_file_processing%'")
"""
    ekd_ftp_uploader_table = """
ekd_ftp_uploader=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_ftp_uploader%'")
"""
    ekd_notification_table = """
ekd_notif=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_notification%'")
"""
    ekd_request_logger_table = """
ekd_req=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_request_logger%'")
"""
    ekd_session_table = """
ekd_session=$($docker_pfx psql -A -t -c "SELECT datname FROM pg_database WHERE datname ILIKE '%ekd_session%'")
"""
    ekd_metadata_table = """
ekd_metadata="ekd_metadata"
"""

    command = '\n$docker_pfx psql --dbname ${} -c "{}"\n'

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
        if "ekd_ftp_uploader" in tables:
            out += self.ekd_ftp_uploader_table
        if "ekd_notification" in tables:
            out += self.ekd_notification_table
        if "ekd_request_logger" in tables:
            out += self.ekd_request_logger_table
        if "ekd_session" in tables:
            out += self.ekd_session_table
        if "ekd_metadata" in tables:
            out += self.ekd_metadata_table

        for key, value in sql_scripts.items():
            out += self.command.format(key, value)

        return out


if __name__ == "__main__":
    cstr = Constructor()

    sql = {
        "ekd_ekd": """
    BEGIN;
    UPDATE employee SET dismissed_date = null WHERE id = '074c8ca6-1037-44c5-a4b1-9a4153ee9823'; 
    COMMIT;
        """
    }

    print(cstr.make_script(sql))
