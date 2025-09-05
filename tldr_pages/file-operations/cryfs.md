# cryfs

> A cryptographic filesystem for the cloud. More information: <https://manned.org/cryfs>.

## Examples

### Mount an encrypted filesystem. The initialization wizard will be started on the first execution

```bash
cryfs path/to/cipher_dir path/to/mount_point
```

### Unmount an encrypted filesystem

```bash
cryfs-unmount path/to/mount_point
```

### Automatically unmount after ten minutes of inactivity

```bash
cryfs --unmount-idle 10 path/to/cipher_dir path/to/mount_point
```

### List supported ciphers

```bash
cryfs --show-ciphers
```
