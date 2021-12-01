### postgres_exporter_fs

Simple up state exporter for "Azure Database for PostgreSQL flexible servers"

#### Environment Variables
- `PG_URI`
  - String value, URI to Postgres Flexible Server, default "postgresql://127.0.0.1/postgres"
- `TEST_PERIOD`
  - Numeric value, period between tests in seconds, default 5
- `POSTGRES`
  - Set to True or False to test/ignore Postgres
- `PGBOUNCER`
  - Set to True or False to test/ignore PgBouncer
- `POSTGRES_PORT`
  - Numeric value, port number to connect to Postgres, default 5432
- `PGBOUNCER_PORT`
  - Numeric value, port number to connect to PgBouncer, default 6432
