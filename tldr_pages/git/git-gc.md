# git-gc

> Optimise the local repository by cleaning unnecessary files. More information: <https://git-scm.com/docs/git-gc>.

## Examples

### Optimise the repository

```bash
git gc
```

### Aggressively optimise, takes more time

```bash
git gc --aggressive
```

### Do not prune loose objects (prunes by default)

```bash
git gc --no-prune
```

### Suppress all output

```bash
git gc --quiet
```

### Display help

```bash
git gc --help
```
