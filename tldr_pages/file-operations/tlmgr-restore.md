# tlmgr-restore

> Restore package backups created with `tlmgr backup`. The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`. More information: <https://www.tug.org/texlive/doc/tlmgr.html#restore>.

## Examples

### List all available backup revisions for all packages

```bash
tlmgr restore
```

### List all available backup revisions for a specific package

```bash
tlmgr restore package
```

### Restore a specific revision of a specific package

```bash
tlmgr restore package revision
```

### Restore the latest revision of all backed-up packages

```bash
tlmgr restore --all
```

### Restore a package from a custom backup directory

```bash
tlmgr restore package revision --backupdir path/to/backup_directory
```

### Perform a dry-run and print all taken actions without making them

```bash
tlmgr restore --dry-run package revision
```
