# mysqlsh

> Advanced client for MySQL, supporting SQL, JavaScript, and Python. It offers features for managing InnoDB clusters and document store collections. More information: <https://manned.org/mysqlsh>.

## Examples

### Start MySQL Shell in interactive mode

```bash
mysqlsh
```

### Connect to a MySQL server

```bash
mysqlsh --user username --host hostname --port port
```

### Execute an SQL statement on the server and exit

```bash
mysqlsh --user username --execute 'sql_statement'
```

### Start MySQL Shell in JavaScript mode

```bash
mysqlsh --js
```

### Start MySQL Shell in Python mode

```bash
mysqlsh --py
```

### Import JSON documents into a MySQL collection

```bash
mysqlsh --import path/to/file.json --schema schema_name --collection collection_name
```

### Enable verbose output

```bash
mysqlsh --verbose
```
