# fgrep

> Matches fixed strings in files. Equivalent to `grep -F`. More information: <https://www.gnu.org/software/grep/manual/grep.html>.

## Examples

### Search for an exact string in a file

```bash
fgrep search_string path/to/file
```

### Search only lines that match entirely in one or more files

```bash
fgrep [-x|--line-regexp] search_string path/to/file1 path/to/file2 ...
```

### Count the number of lines that match the given string in a file

```bash
fgrep [-c|--count] search_string path/to/file
```

### Show the line number in the file along with the line matched

```bash
fgrep [-n|--line-number] search_string path/to/file
```

### Display all lines except those that contain the search string

```bash
fgrep [-v|--invert-match] search_string path/to/file
```

### Display filenames whose content matches the search string at least once

```bash
fgrep [-l|--files-with-matches] search_string path/to/file1 path/to/file2 ...
```
