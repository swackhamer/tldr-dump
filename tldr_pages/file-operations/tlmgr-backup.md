# tlmgr-backup

> Manage backups of TeX Live packages. The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`. More information: <https://www.tug.org/texlive/doc/tlmgr.html#backup>.

## Examples

### Make a backup of one or more packages

```bash
tlmgr backup package1 package2 ...
```

### Make a backup of all packages

```bash
tlmgr backup --all
```

### Make a backup to a custom directory

```bash
tlmgr backup package --backupdir path/to/backup_directory
```

### Remove a backup of one or more packages

```bash
tlmgr backup clean package1 package2 ...
```

### Remove all backups

```bash
tlmgr backup clean --all
```
