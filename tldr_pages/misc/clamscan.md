# clamscan

> A virus scanner. More information: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

## Examples

### Scan a file for vulnerabilities

```bash
clamscan path/to/file
```

### Scan all files recursively in a specific directory

```bash
clamscan [-r|--recursive] path/to/directory
```

### Scan data from `stdin`

```bash
command | clamscan -
```

### Specify a virus database file or directory of files

```bash
clamscan [-d|--database] path/to/database_file_or_directory
```

### Scan the current directory and output only infected files

```bash
clamscan [-i|--infected]
```

### Print the scan report to a log file

```bash
clamscan [-l|--log] path/to/log_file
```

### Move infected files to a specific directory

```bash
clamscan --move path/to/quarantine_directory
```

### Remove infected files

```bash
clamscan --remove yes
```
