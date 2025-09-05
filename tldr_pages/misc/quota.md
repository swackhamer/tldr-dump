# quota

> Display users' disk space usage and allocated limits. More information: <https://manned.org/quota>.

## Examples

### Show disk quotas in human-readable units for the current user

```bash
quota [-s|--human-readable]
```

### Verbose output (also display quotas on filesystems where no storage is allocated)

```bash
quota [-v|--verbose]
```

### Quiet output (only display quotas on filesystems where usage is over quota)

```bash
quota [-q|--quiet]
```

### Print quotas for the groups of which the current user is a member

```bash
quota [-g|--group]
```

### Show disk quotas for another user

```bash
sudo quota [-u|--user] username
```
