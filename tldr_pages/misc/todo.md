# todo

> A simple, standards-based, cli todo manager. More information: <https://todoman.readthedocs.io>.

## Examples

### List startable tasks

```bash
todo list --startable
```

### Add a new task to the work list

```bash
todo new thing_to_do --list work
```

### Add a location to a task with a given ID

```bash
todo edit --location location_name task_id
```

### Show details about a task

```bash
todo show task_id
```

### Mark tasks with the specified IDs as completed

```bash
todo done task_id1 task_id2 ...
```

### Delete a task

```bash
todo delete task_id
```

### Delete done tasks and reset the IDs of the remaining tasks

```bash
todo flush
```
