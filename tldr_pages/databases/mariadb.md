# mariadb

> The mariadb client tool. More information: <https://mariadb.com/kb/en/mariadb-command-line-client/>.

## Examples

### Connect to a specific MariaDB database

```bash
mariadb db_name
```

### Connect to a specific MariaDB database using username and password

```bash
mariadb --user user_name --password your_password db_name
```

### Show warnings after every statement in interactive and batch mode

```bash
mariadb --show-warning
```

### Display less verbose outputs (can be used multiple times to produce less output)

```bash
mariadb -s|-ss|-sss|--silent
```

### Execute SQL statements from a script file

```bash
mariadb db_name < path/to/script.sql > path/to/output.tab
```

### Check memory and open file usage at exit

```bash
mariadb --debug-check
```

### Connect using a socket file for local connections

```bash
mariadb [-S|--socket] path/to/socket_name
```

### Display help

```bash
mariadb [-?|--help]
```
