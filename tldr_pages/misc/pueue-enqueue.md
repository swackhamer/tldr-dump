# pueue-enqueue

> Enqueue stashed tasks. See also: `pueue stash`. More information: <https://github.com/Nukesor/pueue>.

## Examples

### Enqueue multiple stashed tasks at once

```bash
pueue enqueue task_id task_id
```

### Enqueue a stashed task after 60 seconds

```bash
pueue enqueue [-d|--delay] 60 task_id
```

### Enqueue a stashed task next Wednesday

```bash
pueue enqueue [-d|--delay] wednesday task_id
```

### Enqueue a stashed task after four months

```bash
pueue enqueue [-d|--delay] "4 months" task_id
```

### Enqueue a stashed task on 2021-02-19

```bash
pueue enqueue [-d|--delay] 2021-02-19 task_id
```

### List all available date/time formats

```bash
pueue enqueue [-h|--help]
```
