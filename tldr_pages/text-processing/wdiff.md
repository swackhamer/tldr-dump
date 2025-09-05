# wdiff

> Display word differences between text files. More information: <https://www.gnu.org/software/wdiff/manual/wdiff.html#wdiff-invocation>.

## Examples

### Compare two files

```bash
wdiff path/to/file1 path/to/file2
```

### Ignore case when comparing

```bash
wdiff [-i|--ignore-case] path/to/file1 path/to/file2
```

### Display how many words are deleted, inserted or replaced

```bash
wdiff [-s|--statistics] path/to/file1 path/to/file2
```
