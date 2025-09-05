# transcrypt

> Transparently encrypt files within a Git repository. More information: <https://github.com/elasticdog/transcrypt>.

## Examples

### Initialize an unconfigured repository

```bash
transcrypt
```

### List the currently encrypted files

```bash
git ls-crypt
```

### Display the credentials of a configured repository

```bash
transcrypt [-d|--display]
```

### Initialize and decrypt a fresh clone of a configured repository

```bash
transcrypt [-c|--cipher] cipher
```

### Rekey to change the encryption cipher or password

```bash
transcrypt [-r|--rekey]
```
