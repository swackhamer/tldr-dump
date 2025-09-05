# todoist

> Access <https://todoist.com> from the command-line. More information: <https://github.com/sachaos/todoist>.

## Examples

### Add a task

```bash
todoist add "task_name"
```

### Add a high priority task with a label, project, and due date

```bash
todoist add "task_name" --priority 1 --label-ids "label_id" --project-name "project_name" --date "tmr 9am"
```

### Add a high priority task with a label, project, and due date in quick mode

```bash
todoist quick '#project_name "tmr 9am" p1 task_name @label_name'
```

### List all tasks with a header and color

```bash
todoist --header --color list
```

### List all high priority tasks

```bash
todoist list --filter p1
```

### List today's tasks with high priority that have the specified label

```bash
todoist list --filter '(@label_name | today) & p1'
```
