# pocount

> Translate Toolkit utility to get translation progress from file, supporting several formats. More information: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

## Examples

### Print a colorful table with the translation progress of a file

```bash
pocount path/to/file/file.po
```

### Print translation progress of various files, one line per file

```bash
pocount --short translation_*.ts
```

### Generate a CSV file with the translation progress of various files

```bash
pocount --csv translation_*.ts > path/to/translation_progress.csv
```
