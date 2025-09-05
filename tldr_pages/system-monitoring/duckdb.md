# duckdb

> Client for DuckDB, an in-process analytical SQL engine. More information: <https://duckdb.org>.

## Examples

### Start an interactive shell with a transient in-memory database

```bash
duckdb
```

### Start an interactive shell on a database file. If the file does not exist, a new database is created

```bash
duckdb path/to/dbfile
```

### Query a CSV, JSON, or Parquet file using SQL

```bash
duckdb -c "SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'"
```

### Directly query a CSV, JSON, or Parquet file using the `file` view

```bash
duckdb data_source.[csv|csv.gz|json|json.gz|parquet] -c " SELECT * FROM file "
```

### Run an SQL script

```bash
duckdb -f path/to/script.sql
```

### Run query on database file and keep the interactive shell open

```bash
duckdb path/to/dbfile -cmd "SELECT DISTINCT * FROM tbl"
```

### Read CSV from `stdin` and write CSV to `stdout`

```bash
cat path/to/source.csv | duckdb -c "COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)"
```

### Start the DuckDB UI, a web interface with notebooks

```bash
duckdb -ui
```
