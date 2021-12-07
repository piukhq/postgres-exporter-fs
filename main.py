import logging
import re
import sys
from time import sleep

import psycopg2
from prometheus_client import Gauge, start_http_server

from settings import pg, pg_port, pgb, pgb_port, tp, uri

logging.basicConfig(format="%(asctime)s %(message)s", stream=sys.stdout, level=logging.INFO)

if pg:
    pg_metric = Gauge("postgres_up_state", "Flexible Server Postgres Up State")
if pgb:
    pgb_metric = Gauge("pgbouncer_up_state", "Flexible Server PgBouncer Up State")


def mask_uri(connection_string):
    uri_regex = (
        r"[a-z]+\:\/\/(?P<user>[a-z]+):(?P<password>[A-z0-9]+)@(?P<host>[a-z.-]+)"
        r"\/(?P<dbname>[a-z]+)\?sslmode=(?P<sslmode>[a-z]+)"
    )
    search = re.search(uri_regex, connection_string)
    if search is None:
        return connection_string
    else:
        masked_uri = (
            f"postgresql://{search['user']}:***@{search['host']}/{search['dbname']}?sslmode={search['sslmode']}"
        )
        return masked_uri


def check_vars():
    if not pg and not pgb:
        logging.info("Neither POSTGRES or PGBOUNCER environment variables are set to True")
        logging.info("Nothing to check so exiting")
        exit()


def update_metric(status, type):
    if type == "Postgres":
        pg_metric.set(status)
        logging.info(f"{type} up state set to {status}")
    elif type == "PgBouncer":
        pgb_metric.set(status)
        logging.info(f"{type} up state set to {status}")
    else:
        logging.info("Something went wrong. Metric not set")


def postgres_connect(port, type):
    try:
        connection = psycopg2.connect(uri, port=port)
        logging.info(f"Connected to {mask_uri(uri)}")
    except Exception as error:
        logging.info(f"Connection to Postgres failed - {error}")
        update_metric(0, type)

    else:
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        response = cursor.fetchone()

        if response != (1,):
            update_metric(0, type)

        cursor.close()
        connection.close()
        logging.info(f"Disconnected from {mask_uri(uri)}")
        update_metric(1, type)


if __name__ == "__main__":
    check_vars()
    start_http_server(9100)
    while True:
        if pg:
            postgres_connect(pg_port, "Postgres")
        else:
            logging.info("POSTGRES environment variable not set to True")

        if pgb:
            postgres_connect(pgb_port, "PgBouncer")
        else:
            logging.info("PGBOUNCER environment variable not set to True")

        sleep(tp)
