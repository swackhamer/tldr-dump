# onefetch

> Display project information and code statistics for a local Git repository. More information: <https://github.com/o2sh/onefetch/wiki/command-line-options>.

## Examples

### Display statistics for the Git repository in the current working directory

```bash
onefetch
```

### Display statistics for the Git repository in the specified directory

```bash
onefetch path/to/directory
```

### Ignore commits made by bots

```bash
onefetch --no-bots
```

### Ignore merge commits

```bash
onefetch --no-merges
```

### Don't print the ASCII art of the language logo

```bash
onefetch --no-art
```

### Show `n` authors, languages, or file churns (default: 3, 6, and 3 respectively)

```bash
onefetch --number-of-authors|languages|file-churns n
```

### Ignore the specified files and directories

```bash
onefetch [-e|--exclude] path/to/file_or_directory|regex
```

### Only detect languages from the specified categories (default: programming and markup)

```bash
onefetch [-T|--type] programming|markup|prose|data
```
