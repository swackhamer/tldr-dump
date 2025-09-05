# q

> Execute SQL-like queries on CSV and TSV files. More information: <https://harelba.github.io/q>.

## Examples

### Query a CSV file by specifying the delimiter as ','

```bash
q [-d|--delimiter] ',' "SELECT * from path/to/file"
```

### Query a TSV file

```bash
q [-t|--tab-delimited] "SELECT * from path/to/file"
```

### Query file with header row

```bash
q [-d|--delimiter] delimiter [-H|--skip-header] "SELECT * from path/to/file"
```

### Read data from `stdin`; '-' in the query represents the data from `stdin`

```bash
output | q "select * from -"
```

### Join two files (aliased as `f1` and `f2` in the example) on column `c1`, a common column

```bash
q "SELECT * FROM path/to/file f1 JOIN path/to/other_file f2 ON (f1.c1 = f2.c1)"
```

### Format output using an output delimiter with an output header line (Note: Command will output column names based on the input file header or the column aliases overridden in the query)

```bash
q [-D|--output-delimiter] delimiter [-O|--output-header] "SELECT column as alias from path/to/file"
```
