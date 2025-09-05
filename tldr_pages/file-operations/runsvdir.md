# runsvdir

> Run an entire directory of services. More information: <https://manned.org/runsvdir.8>.

## Examples

### Start and manage all services in a directory as the current user

```bash
runsvdir path/to/services
```

### Start and manage all services in a directory as root

```bash
sudo runsvdir path/to/services
```

### Start services in separate sessions

```bash
runsvdir -P path/to/services
```
