# jmtpfs

> FUSE-based filesystem for accessing MTP devices. More information: <https://manned.org/jmtpfs>.

## Examples

### Mount an MTP device to a directory

```bash
jmtpfs path/to/directory
```

### Set mount options

```bash
jmtpfs -o allow_other,auto_unmount path/to/directory
```

### List available MTP devices

```bash
jmtpfs [-l|--listDevices]
```

### If multiple devices are present, mount a specific device

```bash
jmtpfs -device=bus_id,device_id path/to/directory
```

### Unmount MTP device

```bash
fusermount -u path/to/directory
```
