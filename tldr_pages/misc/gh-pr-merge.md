# gh-pr-merge

> Merge GitHub pull requests. More information: <https://cli.github.com/manual/gh_pr_merge>.

## Examples

### Merge the pull request associated with the current branch interactively

```bash
gh pr merge
```

### Merge the specified pull request, interactively

```bash
gh pr merge pr_number
```

### Merge the pull request, removing the branch on both the local and the remote

```bash
gh pr merge [-d|--delete-branch]
```

### Merge the current pull request with the specified merge strategy

```bash
gh pr merge --merge|squash|rebase
```

### Merge the current pull request with the specified merge strategy and commit message

```bash
gh pr merge --merge|squash|rebase [-t|--subject] commit_message
```

### Squash the current pull request into one commit with the message body and merge

```bash
gh pr merge [-s|--squash] [-b|--body] "commit_message_body"
```

### Display help

```bash
gh pr merge --help
```
