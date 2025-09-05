# restic

> A fast, secure and secure backup program. More information: <https://restic.net>.

## Examples

### Initialize a backup repository in the specified local directory

```bash
restic init --repo path/to/repository
```

### Backup a directory to the repository

```bash
restic --repo path/to/repository backup path/to/directory
```

### Show backup snapshots currently stored in the repository

```bash
restic --repo path/to/repository snapshots
```

### Restore a specific backup snapshot to a target directory

```bash
restic --repo path/to/repository restore latest|snapshot_id --target path/to/target
```

### Restore a specific path from a specific backup to a target directory

```bash
restic --repo path/to/repository restore snapshot_id --target path/to/target --include path/to/restore
```

### Clean up the repository and keep only the most recent snapshot of each unique backup

```bash
restic forget --keep-last 1 --prune
```
