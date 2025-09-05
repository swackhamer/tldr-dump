# git-check-ref-format

> Check if a reference name is acceptable, and exit with a non-zero status if it is not. More information: <https://git-scm.com/docs/git-check-ref-format>.

## Examples

### Check the format of the specified reference name

```bash
git check-ref-format refs/head/refname
```

### Print the name of the last branch checked out

```bash
git check-ref-format --branch @{-1}
```

### Normalize a refname

```bash
git check-ref-format --normalize refs/head/refname
```
