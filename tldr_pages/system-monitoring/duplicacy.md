# duplicacy

> A lock-free deduplication cloud backup tool. More information: <https://github.com/gilbertchen/duplicacy/wiki>.

## Examples

### Use current directory as the repository, initialize a SFTP storage and encrypt the storage with a password

```bash
duplicacy init [-e|-encrypt] snapshot_id sftp://user@192.168.2.100/path/to/storage/
```

### Save a snapshot of the repository to the default storage

```bash
duplicacy backup
```

### List snapshots of current repository

```bash
duplicacy list
```

### Restore the repository to a previously saved snapshot

```bash
duplicacy restore -r revision
```

### Check the integrity of snapshots

```bash
duplicacy check
```

### Add another storage to be used for the existing repository

```bash
duplicacy add storage_name snapshot_id storage_url
```

### Prune a specific revision of snapshot

```bash
duplicacy prune -r revision
```

### Prune revisions, keeping one revision every `n` days for all revisions older than `m` days

```bash
duplicacy prune -keep n:m
```
