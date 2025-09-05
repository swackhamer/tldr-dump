# wezterm

> Wez's Terminal Emulator - a powerful cross-platform terminal emulator and multiplexer. Some subcommands such as `cli` have their own usage documentation. More information: <https://wezterm.org/cli/general>.

## Examples

### Start a new Wezterm process and create a window

```bash
wezterm
```

### Establish an `ssh` session in a new Wezterm window

```bash
wezterm ssh user@host:port
```

### Connect to the multiplexer (`wezterm-mux-server`)

```bash
wezterm connect domain_name
```

### Output an image to the terminal

```bash
wezterm imgcat path/to/image
```

### Record a terminal session as an asciicast (by default recordings are saved to `/tmp`)

```bash
wezterm record
```

### Replay an asciicast terminal session

```bash
wezterm replay path/to/cast_file
```

### Specify the configuration file to use (overrides the normal configuration file resolution)

```bash
wezterm --config-file path/to/config_file
```

### Display help

```bash
wezterm help
```
