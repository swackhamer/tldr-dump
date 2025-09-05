# gt

> Create and manage sequences of dependent code changes (stacks) for Git and GitHub. More information: <https://graphite.dev/docs/get-started>.

## Examples

### Initialize `gt` for the repository in the current directory

```bash
gt init
```

### Create a new branch stacked on top of the current branch and commit staged changes

```bash
gt create branch_name
```

### Create a new commit and fix upstack branches

```bash
gt modify -cam commit_message
```

### Force push all branches in the current stack to GitHub and create or update PRs

```bash
gt stack submit
```

### Checkout different branch (prompts interactive mode when branch name is omitted)

```bash
gt co branch_name
```

### Sync stack with remote version (also deletes merged branches)

```bash
gt sync
```

### Log all tracked stacks

```bash
gt log short
```

### Display help for a specified subcommand

```bash
gt subcommand --help
```
