# odps

> Aliyun ODPS (Open Data Processing Service) command-line tool. Some subcommands such as `inst` have their own usage documentation. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Start the command-line with a custom configuration file

```bash
odpscmd --config=odps_config.ini
```

### Switch current project

```bash
use project_name;
```

### Show tables in the current project

```bash
show tables;
```

### Describe a table

```bash
desc table_name;
```

### Show table partitions

```bash
show partitions table_name;
```

### Describe a partition

```bash
desc table_name partition (partition_spec);
```
