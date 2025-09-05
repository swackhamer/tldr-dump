# odps-tunnel

> Data tunnel in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Download table to local file

```bash
tunnel download table_name path/to/file;
```

### Upload local file to a table partition

```bash
tunnel upload path/to/file table_name/partition_spec;
```

### Upload table specifying field and record delimiters

```bash
tunnel upload path/to/file table_name -fd field_delim -rd record_delim;
```

### Upload table using multiple threads

```bash
tunnel upload path/to/file table_name -threads num;
```
