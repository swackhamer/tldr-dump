# ln

> Create links to files and directories. More information: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

## Examples

### Create a symbolic link to a file or directory

```bash
ln [-s|--symbolic] /path/to/file_or_directory path/to/symlink
```

### Overwrite an existing symbolic link to point to a different file

```bash
ln [-sf|--symbolic --force] /path/to/new_file path/to/symlink
```

### Create a hard link to a file

```bash
ln /path/to/file path/to/hardlink
```
