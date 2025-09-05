# git-summary

> Display information about a Git repository. Part of `git-extras`. More information: <https://manned.org/git-summary>.

## Examples

### Display data about a Git repository

```bash
git summary
```

### Display data about a Git repository since a commit-ish

```bash
git summary commit|branch_name|tag_name
```

### Display data about a Git repository, merging committers using different emails into 1 statistic for each author

```bash
git summary --dedup-by-email
```

### Display data about a Git repository, showing the number of lines modified by each contributor

```bash
git summary --line
```
