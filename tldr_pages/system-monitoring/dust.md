# dust

> Give an instant overview of which directories are using disk space. See also: `du`, `ncdu`. More information: <https://github.com/bootandy/dust#usage>.

## Examples

### Display information for the current directory

```bash
dust
```

### Display information about one or more directories

```bash
dust path/to/directory1 path/to/directory2 ...
```

### Display 30 directories (defaults to 21)

```bash
dust [-n|--number-of-lines] 30
```

### Display information for the current directory, up to 3 levels deep

```bash
dust [-d|--depth] 3
```

### Display the largest directories at the top in descending order

```bash
dust [-r|--reverse]
```

### Ignore a file or directory

```bash
dust [-X|--ignore-directory] path/to/file_or_directory
```

### Do not display percent bars and percentages

```bash
dust [-b|--no-percent-bars]
```
