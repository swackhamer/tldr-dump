# fastapi

> Run FastAPI apps which uses Uvicorn under the hood. More information: <https://manned.org/fastapi>.

## Examples

### Run a FastAPI app with automatic reload (for development)

```bash
fastapi run path/to/file.py --reload
```

### Serve your app in both development mode

```bash
fastapi dev path/to/file.py
```

### Specify the host and port to run on

```bash
fastapi run path/to/file.py --host host_address --port port
```

### Set the app variable name (if not `app`) or specify a custom app directory

```bash
fastapi run path/to/file.py --app-dir path/to/app --app custom_app_name
```

### Display help

```bash
fastapi --help
```

### Display help for a subcommand

```bash
fastapi subcommand --help
```
