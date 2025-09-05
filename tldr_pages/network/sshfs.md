# sshfs

> Filesystem client based on SSH. More information: <https://github.com/libfuse/sshfs>.

## Examples

### Mount remote directory

```bash
sshfs username@remote_host:remote_directory mountpoint
```

### Unmount remote directory

```bash
umount mountpoint
```

### Mount remote directory from server with specific port

```bash
sshfs username@remote_host:remote_directory -p 2222
```

### Use compression

```bash
sshfs username@remote_host:remote_directory -C
```

### Follow symbolic links

```bash
sshfs -o follow_symlinks username@remote_host:remote_directory mountpoint
```
