# psgrep

> Search running processes with `grep`. More information: <https://jvz.github.io/psgrep>.

## Examples

### Find process lines containing a specific string

```bash
psgrep process_name
```

### Find process lines containing a specific string, excluding headers

```bash
psgrep -n process_name
```

### Search using a simplified format (PID, user, command)

```bash
psgrep -s process_name
```
