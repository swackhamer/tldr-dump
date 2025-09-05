# difft

> Compare files or directories based on the syntax of the programming language. See also: `delta`, `diff`. More information: <https://difftastic.wilfred.me.uk/introduction.html>.

## Examples

### Compare two files or directories

```bash
difft path/to/file_or_directory1 path/to/file_or_directory2
```

### Only report the presence of differences between the files

```bash
difft --check-only path/to/file1 path/to/file2
```

### Specify the display mode (default is `side-by-side`)

```bash
difft --display side-by-side|side-by-side-show-both|inline|json path/to/file1 path/to/file2
```

### Ignore comments when comparing

```bash
difft --ignore-comments path/to/file1 path/to/file2
```

### Enable/Disable syntax highlighting of source code (default is `on`)

```bash
difft --syntax-highlight on|off path/to/file1 path/to/file2
```

### Do not output anything at all if there are no differences between files

```bash
difft --skip-unchanged path/to/file_or_directory1 path/to/file_or_directory2
```

### Print all programming languages supported by the tool, along with their extensions

```bash
difft --list-languages
```
