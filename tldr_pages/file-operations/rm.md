# rm

> Remove files or directories. See also: `rmdir`. More information: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

## Examples

### Remove specific files

```bash
rm path/to/file1 path/to/file2 ...
```

### Remove specific files ignoring nonexistent ones

```bash
rm [-f|--force] path/to/file1 path/to/file2 ...
```

### Remove specific files interactively prompting before each removal

```bash
rm [-i|--interactive] path/to/file1 path/to/file2 ...
```

### Remove specific files printing info about each removal

```bash
rm [-v|--verbose] path/to/file1 path/to/file2 ...
```

### Remove specific files and directories recursively

```bash
rm [-r|--recursive] path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Remove empty directories (this is considered the safe method)

```bash
rm [-d|--dir] path/to/directory
```
