# gh

> Work seamlessly with GitHub. Some subcommands such as `config` have their own usage documentation. More information: <https://cli.github.com/manual/gh>.

## Examples

### Clone a GitHub repository locally

```bash
gh repo clone owner/repository
```

### Create a new issue

```bash
gh issue create
```

### View and filter the open issues of the current repository

```bash
gh issue list
```

### View an issue in the default web browser

```bash
gh issue view [-w|--web] issue_number
```

### Create a pull request

```bash
gh pr create
```

### View a pull request in the default web browser

```bash
gh pr view [-w|--web] pr_number
```

### Check out a specific pull request locally

```bash
gh pr checkout pr_number
```

### Check the status of a repository's pull requests

```bash
gh pr status
```
