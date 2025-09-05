# git-update-index

> Git command for manipulating the index. More information: <https://git-scm.com/docs/git-update-index>.

## Examples

### Pretend that a modified file is unchanged (`git status` will not show this as changed)

```bash
git update-index --skip-worktree path/to/modified_file
```
