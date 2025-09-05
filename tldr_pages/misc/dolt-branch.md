# dolt-branch

> Manage Dolt branches. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

## Examples

### List local branches (current branch is highlighted by `*`)

```bash
dolt branch
```

### List all local and remote branches

```bash
dolt branch [-A|--all]
```

### Create a new branch based on the current branch

```bash
dolt branch branch_name
```

### Create a new branch with the specified commit as the latest

```bash
dolt branch branch_name commit
```

### Rename a branch

```bash
dolt branch [-m|--move] branch_name1 branch_name2
```

### Duplicate a branch

```bash
dolt branch [-c|--copy] branch_name1 branch_name2
```

### Delete a branch

```bash
dolt branch [-d|--delete] branch_name
```

### Display the name of the current branch

```bash
dolt branch --show-current
```
