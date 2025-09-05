# readlink

> Follow symlinks and get symlink information. More information: <https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html>.

## Examples

### Get the actual file to which the symlink points

```bash
readlink path/to/file
```

### Get the absolute path to a file

```bash
readlink [-f|--canonicalize] path/to/file
```
