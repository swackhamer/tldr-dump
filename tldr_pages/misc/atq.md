# atq

> Show jobs scheduled by `at` or `batch` commands. More information: <https://manned.org/atq>.

## Examples

### Show the current user's scheduled jobs

```bash
atq
```

### Show jobs from the 'a' [q]ueue (queues have single-character names)

```bash
atq -q a
```

### Show jobs of all users (run as superuser)

```bash
sudo atq
```
