# zpool

> Manage ZFS pools. More information: <https://manned.org/zpool>.

## Examples

### Show the configuration and status of all ZFS zpools

```bash
zpool status
```

### Check a ZFS pool for errors (verifies the checksum of EVERY block). Very CPU and disk intensive

```bash
zpool scrub pool_name
```

### List zpools available for import

```bash
zpool import
```

### Import a zpool

```bash
zpool import pool_name
```

### Export a zpool (unmount all filesystems)

```bash
zpool export pool_name
```

### Show the history of all pool operations

```bash
zpool history pool_name
```

### Create a mirrored pool

```bash
zpool create pool_name mirror disk1 disk2 mirror disk3 disk4
```

### Add a cache (L2ARC) device to a zpool

```bash
zpool add pool_name cache cache_disk
```
