# pueue-send

> Send input to a task. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Send input to a running command

```bash
pueue send task_id "input"
```

### Send confirmation to a task expecting y/N (e.g. APT, cp)

```bash
pueue send task_id y
```
