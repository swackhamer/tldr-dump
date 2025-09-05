# git-show-ref

> Git command for listing references. More information: <https://git-scm.com/docs/git-show-ref>.

## Examples

### Show all refs in the repository

```bash
git show-ref
```

### Show only heads references

```bash
git show-ref --branches
```

### Show only tags references

```bash
git show-ref --tags
```

### Verify that a given reference exists

```bash
git show-ref --verify path/to/ref
```
