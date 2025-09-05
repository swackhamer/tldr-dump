# dolt-checkout

> Checkout the work tree or tables to a branch or commit. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

## Examples

### Switch to a branch

```bash
dolt checkout branch_name
```

### Revert unstaged changes to a table

```bash
dolt checkout table
```

### Create new branch and switch to it

```bash
dolt checkout -b branch_name
```

### Create new branch based on a specified commit and switch to it

```bash
dolt checkout -b branch_name commit
```
