# uniq

> Output the unique lines from a input or file. Since it does not detect repeated lines unless they are adjacent, we need to sort them first. More information: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

## Examples

### Display each line once

```bash
sort path/to/file | uniq
```

### Display only unique lines

```bash
sort path/to/file | uniq [-u|--unique]
```

### Display only duplicate lines

```bash
sort path/to/file | uniq [-d|--repeated]
```

### Display number of occurrences of each line along with that line

```bash
sort path/to/file | uniq [-c|--count]
```

### Display number of occurrences of each line, sorted by the most frequent

```bash
sort path/to/file | uniq [-c|--count] | sort [-nr|--numeric-sort --reverse]
```
