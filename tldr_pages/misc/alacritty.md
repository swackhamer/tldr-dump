# alacritty

> Cross-platform, GPU-accelerated terminal emulator. More information: <https://manned.org/alacritty>.

## Examples

### Start a new Alacritty process and create a window

```bash
alacritty
```

### Start the Alacritty daemon (without creating a window)

```bash
alacritty --daemon
```

### Create a new window using the already running Alacritty process

```bash
alacritty msg create-window
```

### Start the shell in a specific directory (also works with `alacritty msg create-window`)

```bash
alacritty --working-directory path/to/directory
```

### Execute a command in a new Alacritty window (also works with `alacritty msg create-window`)

```bash
alacritty [-e|--command] command
```

### Use an alternative configuration file (defaults to `$XDG_CONFIG_HOME/alacritty/alacritty.toml`)

```bash
alacritty --config-file path/to/config.toml
```
