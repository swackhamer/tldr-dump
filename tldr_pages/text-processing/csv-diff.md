# csv-diff

> View differences between two CSV, TSV or JSON files. More information: <https://github.com/simonw/csv-diff>.

## Examples

### Display a human-readable summary of differences between files using a specific column as a unique identifier

```bash
csv-diff path/to/file1.csv path/to/file2.csv --key column_name
```

### Display a human-readable summary of differences between files that includes unchanged values in rows with at least one change

```bash
csv-diff path/to/file1.csv path/to/file2.csv --key column_name --show-unchanged
```

### Display a summary of differences between files in JSON format using a specific column as a unique identifier

```bash
csv-diff path/to/file1.csv path/to/file2.csv --key column_name --json
```
