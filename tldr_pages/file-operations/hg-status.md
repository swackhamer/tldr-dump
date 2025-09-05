# hg-status

> Show files that have changed in the working directory. More information: <https://www.mercurial-scm.org/help/commands/status>.

## Examples

### Display the status of changed files

```bash
hg status
```

### Display only modified files

```bash
hg status [-m|--modified]
```

### Display only added files

```bash
hg status [-a|--added]
```

### Display only removed files

```bash
hg status [-r|--removed]
```

### Display only deleted (but tracked) files

```bash
hg status [-d|--deleted]
```

### Display changes in the working directory compared to a specified changeset

```bash
hg status --rev revision
```

### Display only files matching a specified glob pattern

```bash
hg status [-I|--include] pattern
```

### Display files, excluding those that match a specified glob pattern

```bash
hg status [-X|--exclude] pattern
```
