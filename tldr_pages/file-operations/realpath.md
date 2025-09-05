# realpath

> Display the resolved absolute path for a file or directory. More information: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

## Examples

### Display the absolute path for a file or directory

```bash
realpath path/to/file_or_directory
```

### Require all path components to exist

```bash
realpath [-e|--canonicalize-existing] path/to/file_or_directory
```

### Resolve ".." components before symlinks

```bash
realpath [-L|--logical] path/to/file_or_directory
```

### Disable symlink expansion

```bash
realpath [-s|--no-symlinks] path/to/file_or_directory
```

### Suppress error messages

```bash
realpath [-q|--quiet] path/to/file_or_directory
```
