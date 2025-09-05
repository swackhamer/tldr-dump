# gocryptfs

> Encrypted overlay filesystem written in Go. More information: <https://github.com/rfjakob/gocryptfs#use>.

## Examples

### Initialize an encrypted filesystem

```bash
gocryptfs -init path/to/cipher_dir
```

### Mount an encrypted filesystem

```bash
gocryptfs path/to/cipher_dir path/to/mount_point
```

### Mount with the explicit master key instead of password

```bash
gocryptfs --masterkey path/to/cipher_dir path/to/mount_point
```

### Change the password

```bash
gocryptfs --passwd path/to/cipher_dir
```

### Make an encrypted snapshot of a plain directory

```bash
gocryptfs --reverse path/to/plain_dir path/to/cipher_dir
```
