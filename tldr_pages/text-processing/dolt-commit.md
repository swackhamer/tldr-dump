# dolt-commit

> Commit staged changes to tables. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-commit>.

## Examples

### Commit all staged changes, opening the editor specified by `$EDITOR` to enter the commit message

```bash
dolt commit
```

### Commit all staged changes with the specified message

```bash
dolt commit [-m|--message] "commit_message"
```

### Stage all unstaged changes to tables before committing

```bash
dolt commit [-a|--all]
```

### Use the specified ISO 8601 commit date (defaults to current date and time)

```bash
dolt commit --date "2021-12-31T00:00:00"
```

### Use the specified author for the commit

```bash
dolt commit --author "author_name <author_email>"
```

### Allow creating an empty commit, with no changes

```bash
dolt commit --allow-empty
```

### Ignore foreign key warnings

```bash
dolt commit [-f|--force]
```
