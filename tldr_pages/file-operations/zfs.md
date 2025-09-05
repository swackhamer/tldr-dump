# zfs

> Manage ZFS filesystems. More information: <https://manned.org/zfs>.

## Examples

### List all available zfs filesystems

```bash
zfs list
```

### Create a new ZFS filesystem

```bash
zfs create pool_name/filesystem_name
```

### Delete a ZFS filesystem

```bash
zfs destroy pool_name/filesystem_name
```

### Create a Snapshot of a ZFS filesystem

```bash
zfs snapshot pool_name/filesystem_name@snapshot_name
```

### Enable compression on a filesystem

```bash
zfs set compression=on pool_name/filesystem_name
```

### Change mountpoint for a filesystem

```bash
zfs set mountpoint=/path/to/mount_point pool_name/filesystem_name
```
