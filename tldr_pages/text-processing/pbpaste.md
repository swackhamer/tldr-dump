# pbpaste

> Send the contents of the clipboard to `stdout`. Comparable to pressing `<Cmd v>` on the keyboard. More information: <https://keith.github.io/xcode-man-pages/pbcopy.1>.

## Examples

### Write the contents of the clipboard to a file

```bash
pbpaste > path/to/file
```

### Use the contents of the clipboard as input to a command

```bash
pbpaste | grep foo
```
