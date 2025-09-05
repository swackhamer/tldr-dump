# gh-pr

> Manage GitHub pull requests. Some subcommands such as `create` have their own usage documentation. More information: <https://cli.github.com/manual/gh_pr>.

## Examples

### Create a pull request

```bash
gh pr create
```

### Check out a specific pull request locally

```bash
gh pr checkout pr_number
```

### View the changes made in the pull request for the current branch

```bash
gh pr diff
```

### Approve the pull request for the current branch

```bash
gh pr review [-a|--approve]
```

### Merge the pull request associated with the current branch interactively

```bash
gh pr merge
```

### Edit a pull request interactively

```bash
gh pr edit
```

### Edit the base branch of a pull request

```bash
gh pr edit [-B|--base] branch_name
```

### Check the status of the current repository's pull requests

```bash
gh pr status
```
