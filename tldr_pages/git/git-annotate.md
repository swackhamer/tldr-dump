# git-annotate

> Show commit hash and last author on each line of a file. See `git blame`, which is preferred over `git annotate`. `git annotate` is provided for those familiar with other version control systems. More information: <https://git-scm.com/docs/git-annotate>.

## Examples

### Print a file with the author name and commit hash prepended to each line

```bash
git annotate path/to/file
```

### Print a file with the author email and commit hash prepended to each line

```bash
git annotate [-e|--show-email] path/to/file
```

### Print only rows that match a `regex`

```bash
git annotate -L :regexp path/to/file
```
