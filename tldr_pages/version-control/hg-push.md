# hg-push

> Push changes from the local repository to a specified destination. More information: <https://www.mercurial-scm.org/help/commands/push>.

## Examples

### Push changes to the "default" remote path

```bash
hg push
```

### Push changes to a specified remote repository

```bash
hg push path/to/destination_repository
```

### Push a new branch if it does not exist (disabled by default)

```bash
hg push --new-branch
```

### Specify a specific revision changeset to push

```bash
hg push [-r|--rev] revision
```

### Specify a specific branch to push

```bash
hg push [-b|--branch] branch
```

### Specify a specific bookmark to push

```bash
hg push [-B|--bookmark] bookmark
```
