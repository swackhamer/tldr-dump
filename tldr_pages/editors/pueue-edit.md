# pueue-edit

> Edit the command or path of a stashed or queued task. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Edit a task, see `pueue status` to get the task ID

```bash
pueue edit task_id
```

### Edit the path from which a task is executed

```bash
pueue edit task_id --path
```

### Edit a command with the specified editor

```bash
EDITOR=nano pueue edit task_id
```
