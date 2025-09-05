# uvicorn

> Python ASGI HTTP Server, for asynchronous projects. More information: <https://www.uvicorn.org/settings/>.

## Examples

### Run Python web app

```bash
uvicorn import.path:app_object
```

### Listen on port 8080 on localhost

```bash
uvicorn --host localhost --port 8080 import.path:app_object
```

### Turn on live reload

```bash
uvicorn --reload import.path:app_object
```

### Use 4 worker processes for handling requests

```bash
uvicorn --workers 4 import.path:app_object
```

### Run app over HTTPS

```bash
uvicorn --ssl-certfile cert.pem --ssl-keyfile key.pem import.path:app_object
```
