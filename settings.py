from os import getenv

uri = getenv("PG_URI", "postgresql://127.0.0.1/postgres")
tp = getenv("TEST_PERIOD", 5)
pg = getenv("POSTGRES")
pg_port = getenv("POSTGRES_PORT", 5432)
pgb = getenv("PGBOUNCER")
pgb_port = getenv("PGBOUNCER_PORT", 6432)
