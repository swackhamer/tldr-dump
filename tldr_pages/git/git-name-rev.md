# git-name-rev

> Describe a commit using existing ref names. More information: <https://git-scm.com/docs/git-name-rev>.

## Examples

### Show the name for HEAD

```bash
git name-rev HEAD
```

### Show only the name

```bash
git name-rev --name-only HEAD
```

### Enumerate all matching ref names

```bash
git name-rev --all
```

### Use only tags to name the commit

```bash
git name-rev --tags HEAD
```

### Exit with a non-zero status code instead of printing `undefined` for unknown commits

```bash
git name-rev --no-undefined commit-ish
```

### Show names for multiple commits

```bash
git name-rev HEAD~1 HEAD~2 main
```

### Restrict names to branch refs

```bash
git name-rev --refs refs/heads/ commit-ish
```

### Read commit IDs from `stdin`

```bash
echo "commit-ish" | git name-rev --annotate-stdin
```
