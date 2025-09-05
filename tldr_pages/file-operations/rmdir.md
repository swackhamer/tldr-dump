# rmdir

> Remove directories without files. See also: `rm`. More information: <https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html>.

## Examples

### Remove specific directories

```bash
rmdir path/to/directory1 path/to/directory2 ...
```

### Remove specific nested directories recursively

```bash
rmdir [-p|--parents] path/to/directory1 path/to/directory2 ...
```

### Clean a directory of empty directories

```bash
rmdir *
```
