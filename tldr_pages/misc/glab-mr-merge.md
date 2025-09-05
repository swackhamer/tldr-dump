# glab-mr-merge

> Merge GitLab merge requests. More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/mr/merge.md>.

## Examples

### Merge the merge request associated with the current branch interactively

```bash
glab mr merge
```

### Merge the specified merge request, interactively

```bash
glab mr merge mr_number
```

### Merge the merge request, removing the branch on both the local and the remote

```bash
glab mr merge [-d|--remove-source-branch]
```

### Squash the current merge request into one commit with the message body and merge

```bash
glab mr merge [-s|--squash] [-m|--message] "commit_message_body"
```

### Display help

```bash
glab mr merge --help
```
