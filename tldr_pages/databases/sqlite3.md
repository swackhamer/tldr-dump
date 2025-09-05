# sqlite3

> Interface to SQLite 3, which is a self-contained file-based embedded SQL engine. More information: <https://sqlite.org/cli.html>.

## Examples

### Start an interactive shell with a new database

```bash
sqlite3
```

### Open an interactive shell against an existing database

```bash
sqlite3 path/to/database.sqlite3
```

### Execute an SQL statement against a database and then exit

```bash
sqlite3 path/to/database.sqlite3 'SELECT * FROM some_table;'
```
