# pgcli

> A modern PostgreSQL CLI with auto-completion and syntax highlighting. More information: <https://www.pgcli.com>.

## Examples

### Connect to a PostgreSQL database using a connection string

```bash
pgcli postgresql://user@host/database
```

### Connect to a database using flags

```bash
pgcli [-h|--host] host [-U|--username] username [-d|--dbname] database
```

### Display help

```bash
pgcli --help
```
