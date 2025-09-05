# zdb

> ZFS debugger. More information: <https://manned.org/zdb>.

## Examples

### Show detailed configuration of all mounted ZFS zpools

```bash
zdb
```

### Show detailed configuration for a specific ZFS pool

```bash
zdb [-C|--config] poolname
```

### Show statistics about number, size and deduplication of blocks

```bash
zdb [-b|--block-stats] poolname
```
