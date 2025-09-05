# colordiff

> A wrapper around `diff` that produces the same output but with pretty syntax highlighting. Color schemes can be customized. More information: <https://github.com/kimmel/colordiff>.

## Examples

### Compare files

```bash
colordiff file1 file2
```

### Output in two columns

```bash
colordiff -y file1 file2
```

### Ignore case differences in file contents

```bash
colordiff -i file1 file2
```

### Report when two files are the same

```bash
colordiff -s file1 file2
```

### Ignore whitespace

```bash
colordiff -w file1 file2
```
