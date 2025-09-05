# rsync

> Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH. To specify a remote path, use `user@host:path/to/file_or_directory`. More information: <https://download.samba.org/pub/rsync/rsync.1>.

## Examples

### Transfer a file

```bash
rsync path/to/source path/to/destination
```

### Use archive mode (recursively copy directories, copy symlinks without resolving, and preserve permissions, ownership and modification times)

```bash
rsync [-a|--archive] path/to/source path/to/destination
```

### Compress the data as it is sent to the destination, display verbose and human-readable progress, and keep partially transferred files if interrupted

```bash
rsync [-zvhP|--compress --verbose --human-readable --partial --progress] path/to/source path/to/destination
```

### Recursively copy directories

```bash
rsync [-r|--recursive] path/to/source path/to/destination
```

### Transfer directory contents, but not the directory itself

```bash
rsync [-r|--recursive] path/to/source/ path/to/destination
```

### Use archive mode, resolve symlinks, and skip files that are newer on the destination

```bash
rsync [-auL|--archive --update --copy-links] path/to/source path/to/destination
```

### Transfer a directory from a remote host running `rsyncd` and delete files on the destination that do not exist on the source

```bash
rsync [-r|--recursive] --delete rsync://host:path/to/source path/to/destination
```

### Transfer a file over SSH using a different port than the default (22) and show global progress

```bash
rsync [-e|--rsh] 'ssh -p port' --info=progress2 host:path/to/source path/to/destination
```
