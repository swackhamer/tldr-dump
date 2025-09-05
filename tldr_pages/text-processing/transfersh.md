# transfersh

> An unofficial client for transfer.sh. More information: <https://github.com/AlpixTM/transfersh>.

## Examples

### Upload a file to transfer.sh

```bash
transfersh path/to/file
```

### Upload a file showing a progress bar (requires Python package `requests_toolbelt`)

```bash
transfersh --progress path/to/file
```

### Upload a file using a different file name

```bash
transfersh --name filename path/to/file
```

### Upload a file to a custom transfer.sh server

```bash
transfersh --servername upload.server.name path/to/file
```

### Upload all files from a directory recursively

```bash
transfersh --recursive path/to/directory/
```

### Upload a specific directory as an uncompressed tar

```bash
transfersh -rt path/to/directory
```
