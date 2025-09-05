# mysqld

> Start the MySQL database server. More information: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

## Examples

### Start the MySQL database server

```bash
mysqld
```

### Start the server, printing error messages to the console

```bash
mysqld --console
```

### Start the server, saving logging output to a custom log file

```bash
mysqld --log=path/to/file.log
```

### Print the default arguments and their values and exit

```bash
mysqld --print-defaults
```

### Start the server, reading arguments and values from a file

```bash
mysqld --defaults-file=path/to/file
```

### Start the server and listen on a custom port

```bash
mysqld --port=port
```

### Display help

```bash
mysqld --verbose --help
```
