# fselect

> Find files with SQL-like queries. More information: <https://github.com/jhspetersson/fselect>.

## Examples

### Select full path and size from temporary or configuration files in a given directory

```bash
fselect size, path from path/to/directory where name = '*.cfg' or name = '*.tmp'
```

### Find square images

```bash
fselect path from path/to/directory where width = height
```

### Find old-school rap 320kbps MP3 files

```bash
fselect path from path/to/directory where genre = Rap and bitrate = 320 and mp3_year lt 2000
```

### Select only the first 5 results and output as JSON

```bash
fselect size, path from path/to/directory limit 5 into json
```

### Use SQL aggregate functions to calculate minimum, maximum and average size of files in a directory

```bash
fselect "MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*) from path/to/directory"
```
