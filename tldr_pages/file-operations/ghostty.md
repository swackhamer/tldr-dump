# ghostty

> A fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. Note: All options from the configuration file can also be used on the command-line (using `--option=argument`). More information: <https://ghostty.org/docs/config/reference>.

## Examples

### Open a new Ghostty window (not supported on macOS)

```bash
ghostty
```

### Run a specific command in a new Ghostty window (not supported on macOS)

```bash
ghostty -e command
```

### List all default and configured keybindings

```bash
ghostty +list-keybinds
```

### List all actions (i.e. what can be triggered via keybindings)

```bash
ghostty +list-actions
```

### Browse an interactive list of themes

```bash
ghostty +list-themes
```

### Print the default configuration (including comments)

```bash
ghostty +show-config --default --docs
```
