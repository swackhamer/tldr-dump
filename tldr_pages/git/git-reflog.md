# git-reflog

> Show a log of changes to local references like HEAD, branches or tags. More information: <https://git-scm.com/docs/git-reflog>.

## Examples

### Show the reflog for HEAD

```bash
git reflog
```

### Show the reflog for a given branch

```bash
git reflog branch_name
```

### Show only the 5 latest entries in the reflog

```bash
git reflog [-n|--max-count] 5
```
