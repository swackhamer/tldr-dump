# mycli

> A CLI for MySQL, MariaDB, and Percona that can do auto-completion and syntax highlighting. More information: <https://manned.org/mycli>.

## Examples

### Connect to a local database on port 3306, using the current user's username

```bash
mycli database_name
```

### Connect to a database (user will be prompted for a password)

```bash
mycli [-u|--user] username database_name
```

### Connect to a database on another host

```bash
mycli [-h|--host] database_host [-P|--port] port [-u|--user] username database_name
```
