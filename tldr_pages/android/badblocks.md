# badblocks

> Search a device for bad blocks. Some usages of badblocks can cause destructive actions, such as erasing all data on a disk, including the partition table. More information: <https://manned.org/badblocks>.

## Examples

### Search a disk for bad blocks by using a non-destructive read-only test

```bash
sudo badblocks /dev/sdX
```

### Search an unmounted disk for bad blocks with a [n]on-destructive read-write test

```bash
sudo badblocks -n /dev/sdX
```

### Search an unmounted disk for bad blocks with a destructive [w]rite test

```bash
sudo badblocks -w /dev/sdX
```

### Use the destructive [w]rite test and [s]how [v]erbose progress

```bash
sudo badblocks -svw /dev/sdX
```

### In destructive mode, [o]utput found blocks to a file

```bash
sudo badblocks -o path/to/file -w /dev/sdX
```

### Use the destructive mode with improved speed using 4K [b]lock size and 64K block [c]ount

```bash
sudo badblocks -w -b 4096 -c 65536 /dev/sdX
```
