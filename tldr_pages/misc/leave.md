# leave

> Set a reminder for when it's time to leave. To remove reminders use `kill $(pidof leave)`. More information: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

## Examples

### Set a reminder at a given time

```bash
leave time_to_leave
```

### Set a reminder to leave at noon

```bash
leave 1200
```

### Set a reminder in a specific amount of time

```bash
leave +amount_of_time
```

### Set a reminder to leave in 4 hours and 4 minutes

```bash
leave +0404
```
