# hub-issue

> Manage Github issues. More information: <https://hub.github.com/hub-issue.1.html>.

## Examples

### List the last 10 issues with the `bug` label

```bash
hub issue list [-L|--limit] 10 [-l|--labels] "bug"
```

### Display a specific issue

```bash
hub issue show issue_number
```

### List 10 closed issues assigneed to a specific user

```bash
hub issue [-s|--state] closed [-a|--assignee] username --limit 10
```
