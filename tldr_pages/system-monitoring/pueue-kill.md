# pueue-kill

> Kill running tasks or whole groups. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Kill all tasks in the default group

```bash
pueue kill
```

### Kill a specific task

```bash
pueue kill task_id
```

### Kill a task and terminate all its child processes

```bash
pueue kill --children task_id
```

### Kill all tasks in a group and pause the group

```bash
pueue kill [-g|--group] group_name
```

### Kill all tasks across all groups and pause all groups

```bash
pueue kill [-a|--all]
```
