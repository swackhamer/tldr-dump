# hg-log

> Display the revision history of the repository. More information: <https://www.mercurial-scm.org/help/commands/log>.

## Examples

### Display the entire revision history of the repository

```bash
hg log
```

### Display the revision history with an ASCII graph

```bash
hg log [-G|--graph]
```

### Display the revision history with file names matching a specified pattern

```bash
hg log [-I|--include] pattern
```

### Display the revision history, excluding file names that match a specified pattern

```bash
hg log [-X|--exclude] pattern
```

### Display the log information for a specific revision

```bash
hg log [-r|--rev] revision
```

### Display the revision history for a specific branch

```bash
hg log [-b|--branch] branch
```

### Display the revision history for a specific date

```bash
hg log [-d|--date] date
```

### Display revisions committed by a specific user

```bash
hg log [-u|--user] user
```
