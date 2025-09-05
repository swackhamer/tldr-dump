# usleep

> Delay execution for a specific interval in microseconds. Largely deprecated in favor of `nanosleep`. See also: `sleep`, `nanosleep`. More information: <https://manned.org/usleep.1>.

## Examples

### Delay in microseconds

```bash
usleep microseconds
```

### Execute a specific command after a 500,000 microseconds delay

```bash
usleep 500000 && command
```
