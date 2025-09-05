# zipcloak

> Encrypt the contents within a Zip archive. More information: <https://manned.org/zipcloak>.

## Examples

### Encrypt the contents of a Zip archive

```bash
zipcloak path/to/archive.zip
```

### Decrypt the contents of a Zip archive

```bash
zipcloak [-d|--decrypt] path/to/archive.zip
```

### Output the encrypted contents into a new Zip archive

```bash
zipcloak path/to/archive.zip [-O|--output-file] path/to/encrypted.zip
```
