# git-secret

> Stores private data inside a Git repository. Written in Bash. More information: <https://github.com/sobolevn/git-secret>.

## Examples

### Initialize `git-secret` in a local repository

```bash
git secret init
```

### Grant access to the current Git user's email

```bash
git secret tell -m
```

### Grant access by email

```bash
git secret tell email
```

### Revoke access by email

```bash
git secret killperson email
```

### List emails with access to secrets

```bash
git secret whoknows
```

### Register a secret file

```bash
git secret add path/to/file
```

### Encrypt secrets

```bash
git secret hide
```

### Decrypt secret files

```bash
git secret reveal
```
