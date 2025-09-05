# dcfldd

> Enhanced version of dd for forensics and security. More information: <https://manned.org/dcfldd>.

## Examples

### Copy a disk to a raw image file and hash the image using SHA256

```bash
dcfldd if=/dev/disk_device of=file.img hash=sha256 hashlog=file.hash
```

### Copy a disk to a raw image file, hashing each 1 GB chunk

```bash
dcfldd if=/dev/disk_device of=file.img hash=sha512|sha384|sha256|sha1|md5 hashlog=file.hash hashwindow=1G
```
