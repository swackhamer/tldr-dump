# rclone

> Copy, synchronize or move files and directories to and from many cloud services. More information: <https://rclone.org>.

## Examples

### Launch an interactive menu to setup rclone

```bash
rclone config
```

### List contents of a directory on an rclone remote

```bash
rclone lsf remote_name:path/to/directory
```

### Copy a file or directory from the local machine to the remote destination

```bash
rclone copy path/to/source_file_or_directory remote_name:path/to/directory
```

### Copy files changed within the past 24 hours to a remote from the local machine, asking the user to confirm each file

```bash
rclone copy [-i|--interactive] --max-age 24h remote_name:path/to/directory path/to/local_directory
```

### Mirror a specific file or directory (Note: Unlike copy, sync removes files from the remote if it does not exist locally)

```bash
rclone sync path/to/file_or_directory remote_name:path/to/directory
```

### Delete a remote file or directory (Note: `--dry-run` means test, remove it from the command to actually delete)

```bash
rclone [-n|--dry-run] delete remote_name:path/to/file_or_directory
```

### Mount rclone remote (experimental)

```bash
rclone mount remote_name:path/to/directory path/to/mount_point
```

### Unmount rclone remote if `<Ctrl c>` fails (experimental)

```bash
fusermount [-u|--update] path/to/mount_point
```
