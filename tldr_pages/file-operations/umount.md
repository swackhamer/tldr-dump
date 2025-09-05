# umount

> Unlink a filesystem from its mount point, making it no longer accessible. A filesystem cannot be unmounted when it is busy. More information: <https://man.openbsd.org/umount>.

## Examples

### Unmount a filesystem, by passing the path to the source it is mounted from

```bash
umount path/to/device_file
```

### Unmount a filesystem, by passing the path to the target where it is mounted

```bash
umount path/to/mounted_directory
```

### Unmount all mounted filesystems (except the `proc` filesystem)

```bash
umount -a
```
