# git-rev-parse

> Display metadata related to revisions. More information: <https://git-scm.com/docs/git-rev-parse>.

## Examples

### Get the commit hash of a branch

```bash
git rev-parse branch_name
```

### Get the current branch name

```bash
git rev-parse --abbrev-ref HEAD
```

### Get the absolute path to the root directory

```bash
git rev-parse --show-toplevel
```
