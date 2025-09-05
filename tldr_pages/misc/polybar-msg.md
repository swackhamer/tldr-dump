# polybar-msg

> Control `polybar` using inter-process-messaging (IPC). Note: IPC is disabled by default and can be enabled by setting `enable-ipc = true` in the Polybar config. More information: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

## Examples

### Quit the bar

```bash
polybar-msg cmd quit
```

### Restart the bar in-place

```bash
polybar-msg cmd restart
```

### Hide the bar (does nothing if the bar is already hidden)

```bash
polybar-msg cmd hide
```

### Show the bar again (does nothing if the bar is not hidden)

```bash
polybar-msg cmd show
```

### Toggle between hidden/visible

```bash
polybar-msg cmd toggle
```

### Execute a module action (the data string is optional)

```bash
polybar-msg action "#module_name.action_name.data_string"
```

### Only send messages to a specific Polybar instance (all instances by default)

```bash
polybar-msg -p pid cmd|action payload
```
