# mysqlbinlog

> Utility for processing MySQL binary log files. More information: <https://dev.mysql.com/doc/refman/en/mysqlbinlog.html>.

## Examples

### Show events from a specific binary log file

```bash
mysqlbinlog path/to/binlog
```

### Show entries from a binary log for a specific database

```bash
mysqlbinlog --database database_name path/to/binlog
```

### Show events from a binary log between specific dates

```bash
mysqlbinlog --start-datetime='2022-01-01 01:00:00' --stop-datetime='2022-02-01 01:00:00' path/to/binlog
```

### Show events from a binary log between specific positions

```bash
mysqlbinlog --start-position=100 --stop-position=200 path/to/binlog
```

### Show binary log from a MySQL server on the given host

```bash
mysqlbinlog --host=hostname path/to/binlog
```
