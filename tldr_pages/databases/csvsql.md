# csvsql

> Generate SQL statements for a CSV file or execute those statements directly on a database. Included in csvkit. More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

## Examples

### Generate a `CREATE TABLE` SQL statement for a CSV file

```bash
csvsql path/to/data.csv
```

### Import a CSV file into an SQL database

```bash
csvsql --insert --db "mysql://user:password@host/database" data.csv
```

### Run an SQL query on a CSV file

```bash
csvsql --query "select * from 'data'" data.csv
```
