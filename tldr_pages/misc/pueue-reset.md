# pueue-reset

> Kill everything and reset. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Kill all tasks and remove everything (logs, status, groups, task IDs)

```bash
pueue reset
```

### Kill all tasks, terminate their children, and reset everything

```bash
pueue reset --children
```

### Reset without asking for confirmation

```bash
pueue reset [-f|--force]
```
