# rsql

> SQL client to interface with databases and other data sources inside the terminal. More information: <https://github.com/theseus-rs/rsql>.

## Examples

### Enter interactive mode

```bash
rsql
```

### Connect to a database (e.g. PostgreSQL)

```bash
rsql --url "postgresql://user:pass@localhost/mydb"
```

### Connect to a PostgreSQL database with SSL

```bash
rsql --url "postgresql://user:pass@localhost/db?sslmode=require"
```

### Connect to a MySQL database with a specified charset

```bash
rsql --url "mysql://user:pass@localhost/db?charset=utf8mb4"
```

### Run a query and exit

```bash
rsql --url "sqlite://database.db" -- "SELECT * FROM users LIMIT 10"
```

### Set default format

```bash
rsql --url "sqlite://db.sqlite" --format json
```

### Connect to file and use custom line separator

```bash
rsql --url "delimited://data.txt?separator=|&has_header=true"
```
