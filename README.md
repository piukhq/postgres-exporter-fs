### postgres_exporter_fs

Simple up state exporter for "Azure Database for PostgreSQL flexible servers"

#### Environment Variables
- `PG_URI`
  - String value, URI to Postgres Flexible Server
- `TEST_PERIOD`
  - Numeric value, period between tests in seconds, default 5
- `POSTGRES`
  - Boulean value, set to True or 1 to test Postgres
- `PGBOUNCER`
  - Boulean value, set to True or 1 to test PgBouncer
- `POSTGRES_PORT`
  - Numeric value, port number to connect to Postgres, default 5432
- `PGBOUNCER_PORT`
  - Numeric value, port number to connect to PgBouncer, default 6432
