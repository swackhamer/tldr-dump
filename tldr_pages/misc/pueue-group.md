# pueue-group

> Display, add or remove groups. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Show all groups with their statuses and number of parallel jobs

```bash
pueue group
```

### Add a custom group

```bash
pueue group add "group_name"
```

### Remove a group and move its tasks to the default group

```bash
pueue group remove "group_name"
```
