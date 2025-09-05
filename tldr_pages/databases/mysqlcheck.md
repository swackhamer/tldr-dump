# mysqlcheck

> Check and repair MySQL tables. More information: <https://dev.mysql.com/doc/refman/en/mysqlcheck.html>.

## Examples

### Check a table

```bash
mysqlcheck --check table
```

### Check a table and provide credentials to access it

```bash
mysqlcheck --check table --user username --password password
```

### Repair a table

```bash
mysqlcheck --repair table
```

### Optimize a table

```bash
mysqlcheck --optimize table
```
