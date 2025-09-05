# filebrowser

> Simple HTTP web server to manage files and directories. More information: <https://filebrowser.org>.

## Examples

### Start a new server instance serving the current directory

```bash
filebrowser
```

### Start a new server instance serving a specific root directory

```bash
filebrowser [-r|--root] path/to/directory
```

### Start an instance with different host address (defaults to `127.0.0.1`) and port (defaults to `8080`)

```bash
filebrowser [-a|--address] host [-p|--port] port [-r|--root] path/to/directory
```

### Start an instance with a specified configuration file, storing the application database in a specific location (defaults to `filebrowser.db` on the current directory)

```bash
filebrowser [-c|--config] path/to/file [-d|--database] path/to/database.db [-r|--root] path/to/directory
```

### Set up a different default first-time account username and password (both default to `admin`) when setting up a new instance

```bash
filebrowser --username username --password password [-r|--root] path/to/directory
```

### Set up the maximum amount of image processors used when generating thumbnails (defaults to `4`)

```bash
filebrowser --img-processors 4 [-r|--root] path/to/directory
```

### Disable image thumbnails as well as the Command Runner feature, limiting access for hosted script files from being executed inside the app

```bash
filebrowser --disable-exec --disable-thumbnails [-r|--root] path/to/directory
```

### Disable resizing of image previews as well as detecting file types by reading their headers

```bash
filebrowser --disable-preview-resize --disable-type-detection-by-header [-r|--root] path/to/directory
```
