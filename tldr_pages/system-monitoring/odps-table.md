# odps-table

> Create and modify tables in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Create a table with partition and lifecycle

```bash
create table table_name (col type) partitioned by (col type) lifecycle days;
```

### Create a table based on the definition of another table

```bash
create table table_name like another_table;
```

### Add partition to a table

```bash
alter table table_name add partition (partition_spec);
```

### Delete partition from a table

```bash
alter table table_name drop partition (partition_spec);
```

### Delete table

```bash
drop table table_name;
```
