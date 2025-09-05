# pgrep

> Find or signal processes by name. More information: <https://www.manned.org/pgrep>.

## Examples

### Return PIDs of any running processes with a matching command string

```bash
pgrep process_name
```

### Search for processes including their command-line options

```bash
pgrep [-f|--full] "process_name parameter"
```

### Search for processes run by a specific user

```bash
pgrep [-u|--euid] root process_name
```
