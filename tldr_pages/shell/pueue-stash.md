# pueue-stash

> Stash tasks to prevent them starting automatically. See also: `pueue start`, `pueue enqueue`. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Stash an enqueued task

```bash
pueue stash task_id
```

### Stash multiple tasks at once

```bash
pueue stash task_id task_id
```

### Start a stashed task immediately

```bash
pueue start task_id
```

### Enqueue a task to be executed when preceding tasks finish

```bash
pueue enqueue task_id
```
