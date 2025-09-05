# pg_ctl

> Utility for controlling a PostgreSQL server and database cluster. More information: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

## Examples

### Initialize a new PostgreSQL database cluster

```bash
pg_ctl [-D|--pgdata] data_directory init
```

### Start a PostgreSQL server

```bash
pg_ctl [-D|--pgdata] data_directory start
```

### Stop a PostgreSQL server

```bash
pg_ctl [-D|--pgdata] data_directory stop
```

### Restart a PostgreSQL server

```bash
pg_ctl [-D|--pgdata] data_directory restart
```

### Reload the PostgreSQL server configuration

```bash
pg_ctl [-D|--pgdata] data_directory reload
```
