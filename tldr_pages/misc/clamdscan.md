# clamdscan

> Scan for viruses using the ClamAV Daemon. More information: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

## Examples

### Scan a file or directory for vulnerabilities

```bash
clamdscan path/to/file_or_directory
```

### Scan data from `stdin`

```bash
command | clamdscan -
```

### Scan the current directory and output only infected files

```bash
clamdscan --infected
```

### Print the scan report to a log file

```bash
clamdscan --log path/to/log_file
```

### Move infected files to a specific directory

```bash
clamdscan --move path/to/quarantine_directory
```

### Remove infected files

```bash
clamdscan --remove
```

### Use multiple threads to scan a directory

```bash
clamdscan --multiscan
```

### Pass the file descriptor instead of streaming the file to the daemon

```bash
clamdscan --fdpass
```
