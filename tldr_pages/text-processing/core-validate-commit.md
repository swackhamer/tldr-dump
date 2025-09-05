# core-validate-commit

> Validate commit messages for Node.js core. More information: <https://github.com/nodejs/core-validate-commit>.

## Examples

### Validate the current commit

```bash
core-validate-commit
```

### Validate a specific commit

```bash
core-validate-commit commit_hash
```

### Validate a range of commits

```bash
git rev-list commit_hash..HEAD | xargs core-validate-commit
```

### List all validation rules

```bash
core-validate-commit [-l|--list]
```

### List all valid Node.js subsystems

```bash
core-validate-commit [-ls|--list-subsystem]
```

### Validate the current commit formatting the output in tap format

```bash
core-validate-commit [-t|--tap]
```

### Display help

```bash
core-validate-commit [-h|--help]
```
