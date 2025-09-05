# skate

> Simple and powerful key-value store. More information: <https://github.com/charmbracelet/skate>.

## Examples

### Store a key and a value on the default database

```bash
skate set "key" "value"
```

### Show your keys saved on the default database

```bash
skate list
```

### Delete key and value from the default database

```bash
skate delete "key"
```

### Create a new key and value in a new database

```bash
skate set "key"@"database_name" "value"
```

### Show your keys saved in a non default database

```bash
skate list @"database_name"
```

### Delete key and value from a specific database

```bash
skate delete "key"@"database_name"
```

### Show the databases available

```bash
skate list-dbs
```

### Delete local db and pull down fresh copy from Charm Cloud

```bash
skate reset @"database_name"
```
