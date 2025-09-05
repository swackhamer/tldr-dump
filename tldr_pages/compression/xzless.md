# xzless

> Display text from `xz` and `lzma` compressed files. See also: `less`. More information: <https://manned.org/xzless>.

## Examples

### View a compressed file

```bash
xzless path/to/file
```

### View a compressed file and display line numbers

```bash
xzless --LINE-NUMBERS path/to/file
```

### View a compressed file and quit if the entire file can be displayed on the first screen

```bash
xzless --quit-if-one-screen path/to/file
```
