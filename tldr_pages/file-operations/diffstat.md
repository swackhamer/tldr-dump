# diffstat

> Create a histogram from the output of the `diff` command. More information: <https://manned.org/diffstat>.

## Examples

### Display changes in a histogram

```bash
diff path/to/file1 path/to/file2 | diffstat
```

### Display inserted, deleted and modified changes as a table

```bash
diff path/to/file1 path/to/file2 | diffstat -t
```
