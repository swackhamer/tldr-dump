# join

> Join lines of two sorted files on a common field. More information: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

## Examples

### Join two files on the first (default) field

```bash
join path/to/file1 path/to/file2
```

### Join two files using a comma (instead of a space) as the field separator

```bash
join -t ',' path/to/file1 path/to/file2
```

### Join field3 of file1 with field1 of file2

```bash
join -1 3 -2 1 path/to/file1 path/to/file2
```

### Produce a line for each unpairable line for file1

```bash
join -a 1 path/to/file1 path/to/file2
```

### Join a file from `stdin`

```bash
cat path/to/file1 | join - path/to/file2
```
