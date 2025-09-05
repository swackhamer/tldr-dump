# gh-issue

> Manage GitHub issues. More information: <https://cli.github.com/manual/gh_issue>.

## Examples

### Display a specific issue

```bash
gh issue view issue_number
```

### Display a specific issue in the default web browser

```bash
gh issue view issue_number [-w|--web]
```

### Create a new issue in the default web browser

```bash
gh issue create [-w|--web]
```

### List the last 10 issues with the `bug` label

```bash
gh issue list [-L|--limit] 10 [-l|--label] "bug"
```

### List closed issues made by a specific user

```bash
gh issue list [-s|--state] closed [-A|--author] username
```

### Display the status of issues relevant to the user, in a specific repository

```bash
gh issue status [-R|--repo] owner/repository
```

### Reopen a specific issue

```bash
gh issue reopen issue_number
```
