# pwqgen

> Generate a random passphrase. See also: `libpasswdqc`. More information: <https://manned.org/pwqgen>.

## Examples

### Generate a passphrase

```bash
pwqgen
```

### Generate a passphrase with a specific bit size between 24 and 136

```bash
pwqgen random=bitsize
```

### Use a config file to control password generation

```bash
pwqgen config=path/to/config_file
```

### Display help

```bash
pwqgen [-h|--help]
```

### Display version

```bash
pwqgen --version
```
