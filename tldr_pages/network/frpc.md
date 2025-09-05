# frpc

> Connect to a `frps` server to start proxying connections on the current host. Part of `frp`. More information: <https://github.com/fatedier/frp>.

## Examples

### Start the service, using the default configuration file (assumed to be `frps.ini` in the current directory)

```bash
frpc
```

### Start the service, using the newer TOML configuration file (`frps.toml` instead of `frps.ini`) in the current directory

```bash
frpc [-c|--config] ./frps.toml
```

### Start the service, using a specific configuration file

```bash
frpc [-c|--config] path/to/file
```

### Check if the configuration file is valid

```bash
frpc verify [-c|--config] path/to/file
```

### Print autocompletion setup script for Bash, fish, PowerShell, or Zsh

```bash
frpc completion bash|fish|powershell|zsh
```

### Display version

```bash
frpc [-v|--version]
```
