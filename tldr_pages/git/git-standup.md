# git-standup

> See commits from a specified user. Part of `git-extras`. More information: <https://manned.org/git-standup>.

## Examples

### Show a given author's commits from the last 10 days

```bash
git standup -a name|email -d 10
```

### Show a given author's commits from the last 10 days and whether they are GPG signed

```bash
git standup -a name|email -d 10 -g
```

### Show all the commits from all contributors for the last 10 days

```bash
git standup -a all -d 10
```

### Display help

```bash
git standup -h
```
