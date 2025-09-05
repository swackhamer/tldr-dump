# usql

> Universal CLI interface for SQL databases. More information: <https://github.com/xo/usql>.

## Examples

### Connect to a specific database

```bash
usql sqlserver|mysql|postgres|sqlite3|...://username:password@host:port/database_name
```

### Execute commands from a file

```bash
usql --file=path/to/query.sql
```

### Execute a specific SQL command

```bash
usql --command="sql_command"
```

### Run an SQL command in the `usql` prompt

```bash
prompt=> command
```

### Display the database schema

```bash
prompt=> \d
```

### Export query results to a specific file

```bash
prompt=> \g path/to/file_with_results
```

### Import data from a CSV file into a specific table

```bash
prompt=> \copy path/to/data.csv table_name
```
