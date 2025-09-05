# trunk

> Bundle and serve Rust web apps with CI/CD pipelines. More information: <https://docs.trunk.io/references/cli>.

## Examples

### Start local/production server with hot reloading

```bash
trunk serve --port port --release --proxy-backend URL
```

### Build for production at root or subdirectory

```bash
trunk build --release --dist path/to/distribution --public-url /path/to/app/subdir
```

### List all available tools in the repo and if they are enabled

```bash
trunk tools list
```

### Enable/disable a tool at a specific version

```bash
trunk tools enable|disable tool@version
```

### Print an action's execution history

```bash
trunk actions history action
```
