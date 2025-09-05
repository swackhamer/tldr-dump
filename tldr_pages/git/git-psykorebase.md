# git-psykorebase

> Rebase a branch on top of another using a merge commit and only one conflict handling. Part of `git-extras`. More information: <https://manned.org/git-psykorebase>.

## Examples

### Rebase the current branch on top of another using a merge commit and only one conflict handling

```bash
git psykorebase upstream_branch
```

### Continue after conflicts have been handled

```bash
git psykorebase --continue
```

### Specify the branch to rebase

```bash
git psykorebase upstream_branch target_branch
```
