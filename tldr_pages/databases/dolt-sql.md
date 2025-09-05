# dolt-sql

> Run an SQL query. Multiple SQL statements must be separated by semicolons. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

## Examples

### Run a single query

```bash
dolt sql [-q|--query] "INSERT INTO t values (1, 3);"
```

### List all saved queries

```bash
dolt sql [-l|--list-saved]
```
