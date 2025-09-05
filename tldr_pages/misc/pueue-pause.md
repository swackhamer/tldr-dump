# pueue-pause

> Pause running tasks or groups. See also: `pueue start`. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Pause all tasks in the default group

```bash
pueue pause
```

### Pause a running task

```bash
pueue pause task_id
```

### Pause a running task and stop all its direct children

```bash
pueue pause --children task_id
```

### Pause all tasks in a group and prevent it from starting new tasks

```bash
pueue pause [-g|--group] group_name
```

### Pause all tasks and prevent all groups from starting new tasks

```bash
pueue pause [-a|--all]
```
