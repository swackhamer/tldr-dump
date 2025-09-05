# comm

> Select or reject lines common to two files. Both files must be sorted. More information: <https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

## Examples

### Produce three tab-separated columns: lines only in first file, lines only in second file and common lines

```bash
comm file1 file2
```

### Print only lines common to both files

```bash
comm -12 file1 file2
```

### Print only lines common to both files, reading one file from `stdin`

```bash
cat file1 | comm -12 - file2
```

### Get lines only found in first file, saving the result to a third file

```bash
comm -23 file1 file2 > file1_only
```

### Print lines only found in second file, when the files aren't sorted

```bash
comm -13 <(sort file1) <(sort file2)
```
