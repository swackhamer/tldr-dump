# pueue-start

> Resume operation of tasks or groups of tasks. See also: `pueue pause`. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Resume all tasks in the default group

```bash
pueue start
```

### Resume a specific task

```bash
pueue start task_id
```

### Resume multiple tasks at once

```bash
pueue start task_id task_id
```

### Resume all tasks and start their children

```bash
pueue start [-a|--all] --children
```

### Resume all tasks in a specific group

```bash
pueue start group group_name
```
