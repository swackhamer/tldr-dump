# ftp

> Tools to interact with a server via File Transfer Protocol. More information: <https://manned.org/ftp>.

## Examples

### Connect to an FTP server

```bash
ftp ftp.example.com
```

### Connect to an FTP server specifying its IP address and port

```bash
ftp ip_address port
```

### Switch to binary transfer mode (graphics, compressed files, etc)

```bash
binary
```

### Transfer multiple files without prompting for confirmation on every file

```bash
prompt off
```

### Download multiple files (glob expression)

```bash
mget *.png
```

### Upload multiple files (glob expression)

```bash
mput *.zip
```

### Delete multiple files on the remote server

```bash
mdelete *.txt
```

### Rename a file on the remote server

```bash
rename original_filename new_filename
```
