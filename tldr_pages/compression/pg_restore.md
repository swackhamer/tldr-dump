# pg_restore

> Restore a PostgreSQL database from an archive file created by pg_dump. More information: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

## Examples

### Restore an archive into an existing database

```bash
pg_restore [-d|--dbname] db_name archive_file.dump
```

### Same as above, customize username

```bash
pg_restore [-U|--username] username [-d|--dbname] db_name archive_file.dump
```

### Same as above, customize host and port

```bash
pg_restore [-h|--host] host [-p|--port] port [-d|--dbname] db_name archive_file.dump
```

### List database objects included in the archive

```bash
pg_restore [-l|--list] archive_file.dump
```

### Clean database objects before creating them

```bash
pg_restore [-c|--clean] [-d|--dbname] db_name archive_file.dump
```

### Use multiple jobs to do the restoring

```bash
pg_restore [-j|--jobs] 2 [-d|--dbname] db_name archive_file.dump
```
