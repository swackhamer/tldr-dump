# fdupes

> Finds duplicate files in a set of directories. More information: <https://github.com/adrianlopezroche/fdupes>.

## Examples

### Search a single directory

```bash
fdupes path/to/directory
```

### Search multiple directories

```bash
fdupes directory1 directory2
```

### Search a directory recursively

```bash
fdupes [-r|--recurse] path/to/directory
```

### Search multiple directories, one recursively

```bash
fdupes path/to/irectory1 [-R|--recurse:] path/to/directory2
```

### Search recursively, considering hardlinks as duplicates

```bash
fdupes [-rH|--recurse --hardlinks] path/to/directory
```

### Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others

```bash
fdupes [-rd|--recurse --delete] path/to/directory
```

### Search recursively and delete duplicates without prompting

```bash
fdupes [-rdN|--recurse --delete --noprompt] path/to/directory
```
