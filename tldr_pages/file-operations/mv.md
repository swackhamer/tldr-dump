# mv

> Move or rename files and directories. More information: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

## Examples

### Rename a file or directory when the target is not an existing directory

```bash
mv path/to/source path/to/target
```

### Move a file or directory into an existing directory

```bash
mv path/to/source path/to/existing_directory
```

### Move multiple files into an existing directory, keeping the filenames unchanged

```bash
mv path/to/source1 path/to/source2 ... path/to/existing_directory
```

### Do not prompt for confirmation before overwriting existing files

```bash
mv [-f|--force] path/to/source path/to/target
```

### Prompt for confirmation interactively before overwriting existing files, regardless of file permissions

```bash
mv [-i|--interactive] path/to/source path/to/target
```

### Do not overwrite existing files at the target

```bash
mv [-n|--no-clobber] path/to/source path/to/target
```

### Move files in verbose mode, showing files after they are moved

```bash
mv [-v|--verbose] path/to/source path/to/target
```

### Specify target directory so that you can use external tools to gather movable files

```bash
find /var/log -type f -name '*.log' -print0 | xargs -0 mv [-t|--target-directory] path/to/target_directory
```
