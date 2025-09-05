# sftp

> Secure File Transfer Program. Interactive program to copy files between hosts over SSH. For non-interactive file transfers, see `scp` or `rsync`. More information: <https://manned.org/sftp>.

## Examples

### Connect to a remote server and enter an interactive command mode

```bash
sftp remote_user@remote_host
```

### Connect using an alternate port

```bash
sftp -P remote_port remote_user@remote_host
```

### Connect using a predefined host (in `~/.ssh/config`)

```bash
sftp host
```

### Transfer remote file to the local system

```bash
get path/to/remote_file
```

### Transfer local file to the remote system

```bash
put path/to/local_file
```

### Transfer remote directory to the local system recursively (works with `put` too)

```bash
get -R path/to/remote_directory
```

### Get list of files on local machine

```bash
lls
```

### Get list of files on remote machine

```bash
ls
```
