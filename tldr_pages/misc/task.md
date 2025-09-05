# task

> To-do list manager. More information: <https://taskwarrior.org/docs/>.

## Examples

### Add a new task which is due tomorrow

```bash
task add description due:tomorrow
```

### Update a task's priority

```bash
task task_id modify priority:H|M|L
```

### Complete a task

```bash
task task_id done
```

### Delete a task

```bash
task task_id delete
```

### List all open tasks

```bash
task list
```

### List open tasks due before the end of the week

```bash
task list due.before:eow
```

### Show a graphical burndown chart, by day

```bash
task burndown.daily
```

### List all reports

```bash
task reports
```
