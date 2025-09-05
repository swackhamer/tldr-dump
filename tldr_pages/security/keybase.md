# keybase

> Key directory that maps social media identities to encryption keys in a publicly auditable manner. More information: <https://book.keybase.io/docs/cli>.

## Examples

### Follow another user

```bash
keybase follow username
```

### Add a new proof

```bash
keybase prove service service_username
```

### Sign a file

```bash
keybase sign [-i|--infile] input_file [-o|--outfile] output_file
```

### Verify a signed file

```bash
keybase verify [-i|--infile] input_file [-o|--outfile] output_file
```

### Encrypt a file

```bash
keybase encrypt [-i|--infile] input_file [-o|--outfile] output_file receiver
```

### Decrypt a file

```bash
keybase decrypt [-i|--infile] input_file [-o|--outfile] output_file
```

### Revoke current device, log out, and delete local data

```bash
keybase deprovision
```
