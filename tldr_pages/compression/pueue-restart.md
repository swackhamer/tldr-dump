# pueue-restart

> Restart tasks. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Restart a specific task

```bash
pueue restart task_id
```

### Restart multiple tasks at once, and start them immediately (do not enqueue)

```bash
pueue restart [-k|--immediately] task_id task_id
```

### Restart a specific task from a different path

```bash
pueue restart --edit-path task_id
```

### Edit a command before restarting

```bash
pueue restart [-e|--edit] task_id
```

### Restart a task in-place (without enqueuing as a separate task)

```bash
pueue restart [-i|--in-place] task_id
```

### Restart all failed tasks and stash them

```bash
pueue restart [-a|--all-failed] --stashed
```
