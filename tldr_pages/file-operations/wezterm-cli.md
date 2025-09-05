# wezterm-cli

> Interact with a running Wezterm GUI or multiplexer. More information: <https://wezterm.org/cli/cli/index.html>.

## Examples

### List windows, tabs, and panes

```bash
wezterm cli list
```

### Split the current pane and print the new pane's ID to `stdout`

```bash
wezterm cli split-pane --left|right|top|bottom --cells|percent n
```

### Activate (focus) a pane

```bash
wezterm cli activate-pane --pane-id id
```

### Kill a pane

```bash
wezterm cli kill-pane --pane-id id
```
