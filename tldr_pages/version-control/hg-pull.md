# hg-pull

> Pull changes from a specified repository to the local repository. More information: <https://www.mercurial-scm.org/help/commands/pull>.

## Examples

### Pull from the "default" source path

```bash
hg pull
```

### Pull from a specified source repository

```bash
hg pull path/to/source_repository
```

### Update the local repository to the head of the remote

```bash
hg pull [-u|--update]
```

### Pull changes even when the remote repository is unrelated

```bash
hg pull [-f|--force]
```

### Specify a specific revision changeset to pull up to

```bash
hg pull [-r|--rev] revision
```

### Specify a specific branch to pull

```bash
hg pull [-b|--branch] branch
```

### Specify a specific bookmark to pull

```bash
hg pull [-B|--bookmark] bookmark
```
