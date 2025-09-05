# tb

> Manage tasks and notes across multiple boards. More information: <https://github.com/klaussinani/taskbook>.

## Examples

### Add a new task to a board

```bash
tb --task task_description @board_name
```

### Add a new note to a board

```bash
tb --note note_description @board_name
```

### Edit item's priority

```bash
tb --priority @item_id priority
```

### Check/uncheck item

```bash
tb --check item_id
```

### Archive all checked items

```bash
tb --clear
```

### Move item to a board

```bash
tb --move @item_id board_name
```
