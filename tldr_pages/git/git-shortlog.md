# git-shortlog

> Summarizes the `git log` output. More information: <https://git-scm.com/docs/git-shortlog>.

## Examples

### View a summary of all the commits made, grouped alphabetically by author name

```bash
git shortlog
```

### View a summary of all the commits made, sorted by the number of commits made

```bash
git shortlog [-n|--numbered]
```

### View a summary of all the commits made, grouped by the committer identities (name and email)

```bash
git shortlog [-c|--committer]
```

### View a summary of the last 5 commits (i.e. specify a revision range)

```bash
git shortlog HEAD~5..HEAD
```

### View all users, emails and the number of commits in the current branch

```bash
git shortlog [-s|--summary] [-n|--numbered] [-e|--email]
```

### View all users, emails and the number of commits in all branches

```bash
git shortlog [-s|--summary] [-n|--numbered] [-e|--email] --all
```
