# monodevelop

> Cross platform IDE for C#, F# and more. More information: <https://www.monodevelop.com/documentation/>.

## Examples

### Start MonoDevelop

```bash
monodevelop
```

### Open a specific file

```bash
monodevelop path/to/file
```

### Open a specific file with the caret at a specific position

```bash
monodevelop path/to/file;line_number;column_number
```

### Force opening a new window instead of switching to an existing one

```bash
monodevelop --new-window
```

### Disable redirection of `stdout` and `stderr` to a log file

```bash
monodevelop --no-redirect
```

### Enable performance monitoring

```bash
monodevelop --perf-log
```
