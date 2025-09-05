# pueue-follow

> Follow the output of a currently running task. See also: `pueue log`. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Follow the output of a task (`stdout` + `stderr`)

```bash
pueue follow task_id
```

### Follow `stderr` of a task

```bash
pueue follow --err task_id
```
