# sqlite-utils

> Manipulate SQLite databases in a number of different ways. More information: <https://sqlite-utils.datasette.io/en/stable/cli.html>.

## Examples

### Create a database

```bash
sqlite-utils create-database path/to/database.db
```

### Create a table

```bash
sqlite-utils create-table path/to/database.db table_name id integer name text height float photo blob --pk id
```

### List tables

```bash
sqlite-utils tables path/to/database.db
```

### Upsert a record

```bash
echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]' | sqlite-utils upsert path/to/database.db table_name - --pk id
```

### Select records

```bash
sqlite-utils rows path/to/database.db table_name
```

### Delete a record

```bash
sqlite-utils query path/to/database.db "delete from table_name where name = 'Tony Hoare'"
```

### Drop a table

```bash
sqlite-utils drop-table path/to/database.db table_name
```

### Display help

```bash
sqlite-utils [-h|--help]
```
