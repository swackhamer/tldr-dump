# trap

> Execute a command upon an event. More information: <https://manned.org/trap.1posix>.

## Examples

### List the commands and the names of the expected events

```bash
trap
```

### Execute a command when a signal is received

```bash
trap 'echo "Caught signal SIGHUP"' HUP
```

### Remove commands

```bash
trap - HUP INT
```
