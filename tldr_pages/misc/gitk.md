# gitk

> Browse Git repositories graphically. See also: `git-gui`, `git-cola`, `tig`. More information: <https://git-scm.com/docs/gitk>.

## Examples

### Show the repository browser for the current Git repository

```bash
gitk
```

### Show repository browser for a specific file or directory

```bash
gitk path/to/file_or_directory
```

### Show commits made since 1 week ago

```bash
gitk --since="1 week ago"
```

### Show commits older than 1/1/2016

```bash
gitk --until="1/1/2015"
```

### Show at most 100 changes in all branches

```bash
gitk --max-count=100 --all
```
