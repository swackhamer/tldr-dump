# http-server-upload

> Zero-configuration HTTP server which provides a lightweight interface to upload files. More information: <https://github.com/crycode-de/http-server-upload>.

## Examples

### Start an HTTP server on the default port to upload files to the current directory

```bash
http-server-upload
```

### Start an HTTP server with the specified maximum allowed file size for uploads in MiB (defaults to 200 MiB)

```bash
MAX_FILE_SIZE=size_in_megabytes http-server-upload
```

### Start an HTTP server on a specific port to upload files to the current directory

```bash
PORT=port http-server-upload
```

### Start an HTTP server, storing the uploaded files in a specific directory

```bash
UPLOAD_DIR=path/to/directory http-server-upload
```

### Start an HTTP server using a specific directory to temporarily store files during the upload process

```bash
UPLOAD_TMP_DIR=path/to/directory http-server-upload
```

### Start an HTTP server accepting uploads with a specific token field in the HTTP post

```bash
TOKEN=secret http-server-upload
```
