# gpgv

> Verify OpenPGP signatures. More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

## Examples

### Verify a signed file

```bash
gpgv path/to/file
```

### Verify a signed file using a detached signature

```bash
gpgv path/to/signature path/to/file
```

### Add a file to the list of keyrings (a single exported key also counts as a keyring)

```bash
gpgv --keyring ./alice.keyring path/to/signature path/to/file
```
