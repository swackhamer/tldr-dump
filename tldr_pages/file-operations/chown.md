# chown

> Change user and group ownership of files and directories. More information: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

## Examples

### Change the owner user of a file/directory

```bash
chown user path/to/file_or_directory
```

### Change the owner user and group of a file/directory

```bash
chown user:group path/to/file_or_directory
```

### Change the owner user and group to both have the name `user`

```bash
chown user: path/to/file_or_directory
```

### Recursively change the owner of a directory and its contents

```bash
chown [-R|--recursive] user path/to/directory
```

### Change the owner of a symbolic link

```bash
chown [-h|--no-dereference] user path/to/symlink
```

### Change the owner of a file/directory to match a reference file

```bash
chown --reference path/to/reference_file path/to/file_or_directory
```
