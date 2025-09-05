# yadm-transcrypt

> If `transcrypt` is installed, this command allows you to pass options directly to `transcrypt`. With the environment configured to use the yadm repository. Transcrypt enables transparent encryption and decryption of files in a Git repository. More information: <https://github.com/elasticdog/transcrypt>.

## Examples

### Set the symmetric cipher to utilize for encryption

```bash
yadm transcrypt --cipher=cipher
```

### Pass the password to derive the key from

```bash
yadm transcrypt --password=password
```

### Assume yes and accept defaults for non-specified options

```bash
yadm transcrypt --yes
```

### Display the current repository's cipher and password

```bash
yadm transcrypt --display
```

### Re -encrypt all encrypted files using new credentials

```bash
yadm transcrypt --rekey
```
