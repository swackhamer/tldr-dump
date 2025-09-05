# borg

> Deduplicating backup tool. Create local or remote backups that are mountable as filesystems. More information: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

## Examples

### Initialize a (local) repository

```bash
borg init path/to/repo_directory
```

### Backup a directory into the repository, creating an archive called "Monday"

```bash
borg create --progress path/to/repo_directory::Monday path/to/source_directory
```

### List all archives in a repository

```bash
borg list path/to/repo_directory
```

### Extract a specific directory from the "Monday" archive in a remote repository, excluding all `*.ext` files

```bash
borg extract user@host:path/to/repo_directory::Monday path/to/target_directory --exclude '*.ext'
```

### Prune a repository by deleting all archives older than 7 days, listing changes

```bash
borg prune --keep-within 7d --list path/to/repo_directory
```

### Mount a repository as a FUSE filesystem

```bash
borg mount path/to/repo_directory::Monday path/to/mountpoint
```

### Display help on creating archives

```bash
borg create --help
```
