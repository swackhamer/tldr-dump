# diskutil

> Utility to manage local disks and volumes. Some subcommands such as `partitiondisk` have their own usage documentation. More information: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

## Examples

### List all currently available disks, partitions and mounted volumes

```bash
diskutil list
```

### Repair the filesystem data structures of a volume

```bash
diskutil repairVolume /dev/disk
```

### Unmount a volume

```bash
diskutil unmountDisk /dev/disk
```

### Eject a CD/DVD (unmount first)

```bash
diskutil eject /dev/diskX
```
