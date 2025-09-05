# pueue-parallel

> Set the amount of allowed parallel tasks. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Set the maximum number of tasks allowed to run in parallel, in the default group

```bash
pueue parallel max_number_of_parallel_tasks
```

### Set the maximum number of tasks allowed to run in parallel, in a specific group

```bash
pueue parallel [-g|--group] group_name maximum_number_of_parallel_tasks
```
