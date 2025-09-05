# gh-issue-create

> Create GitHub issues on a repository. More information: <https://cli.github.com/manual/gh_issue_create>.

## Examples

### Create a new issue against the current repository interactively

```bash
gh issue create
```

### Create a new issue with the `bug` label interactively

```bash
gh issue create [-l|--label] "bug"
```

### Create a new issue interactively and assign it to the specified users

```bash
gh issue create [-a|--assignee] user1,user2,...
```

### Create a new issue with a title, body and assign it to the current user

```bash
gh issue create [-t|--title] "title" [-b|--body] "body" [-a|--assignee] "@me"
```

### Create a new issue interactively, reading the body text from a file

```bash
gh issue create [-F|--body-file] path/to/file
```

### Create a new issue in the default web browser

```bash
gh issue create [-w|--web]
```

### Display help

```bash
gh issue create --help
```
