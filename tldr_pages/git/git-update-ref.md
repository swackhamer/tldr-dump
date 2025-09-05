# git-update-ref

> Git command for creating, updating, and deleting Git refs. More information: <https://git-scm.com/docs/git-update-ref>.

## Examples

### Delete a ref, useful for soft resetting the first commit

```bash
git update-ref -d HEAD
```

### Update ref with a message

```bash
git update-ref -m message HEAD 4e95e05
```
