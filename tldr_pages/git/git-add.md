# git-add

> Adds changed files to the index. More information: <https://git-scm.com/docs/git-add>.

## Examples

### Add a file to the index

```bash
git add path/to/file
```

### Add all files (tracked and untracked)

```bash
git add [-A|--all]
```

### Add all files recursively starting from the current folder

```bash
git add .
```

### Only add already tracked files

```bash
git add [-u|--update]
```

### Also add ignored files

```bash
git add [-f|--force]
```

### Interactively stage parts of files

```bash
git add [-p|--patch]
```

### Interactively stage parts of a given file

```bash
git add [-p|--patch] path/to/file
```

### Interactively stage a file

```bash
git add [-i|--interactive]
```
