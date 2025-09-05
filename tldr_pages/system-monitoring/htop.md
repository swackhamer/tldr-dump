# htop

> Display dynamic real-time information about running processes. An enhanced version of `top`. More information: <https://manned.org/htop>.

## Examples

### Start `htop`

```bash
htop
```

### Start `htop` displaying processes owned by a specific user

```bash
htop [-u|--user] username
```

### Display processes hierarchically in a tree view to show the parent-child relationships

```bash
htop [-t|--tree]
```

### Sort processes by a specified `sort_item` (use `htop --sort help` for available options)

```bash
htop [-s|--sort] sort_item
```

### Start `htop` with the specified delay between updates, in tenths of a second (i.e. 50 = 5 seconds)

```bash
htop [-d|--delay] 50
```

### See interactive commands while running htop

```bash
<?>
```

### Switch to a different tab

```bash
<Tab>
```

### Display help

```bash
htop [-h|--help]
```
