# mysql

> The MySQL tool. More information: <https://manned.org/mysql>.

## Examples

### Connect to a database

```bash
mysql database_name
```

### Connect to a database, user will be prompted for a password

```bash
mysql [-u|--user] user [-p|--password] database_name
```

### Connect to a database on another host

```bash
mysql [-h|--host] database_host database_name
```

### Connect to a database through a Unix socket

```bash
mysql [-S|--socket] path/to/socket.sock
```

### Execute SQL statements in a script file (batch file)

```bash
mysql [-e|--execute] "source filename.sql" database_name
```

### Restore a database from a backup created with `mysqldump` (user will be prompted for a password)

```bash
mysql [-u|--user] user [-p|--password] database_name < path/to/backup.sql
```

### Restore all databases from a backup (user will be prompted for a password)

```bash
mysql [-u|--user] user [-p|--password] < path/to/backup.sql
```
