# cp

> Copy files and directories. More information: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

## Examples

### Copy a file to another location

```bash
cp path/to/source_file.ext path/to/target_file.ext
```

### Copy a file into another directory, keeping the filename

```bash
cp path/to/source_file.ext path/to/target_parent_directory
```

### Recursively copy a directory's contents to another location (if the destination exists, the directory is copied inside it)

```bash
cp [-r|--recursive] path/to/source_directory path/to/target_directory
```

### Copy a directory recursively, in verbose mode (shows files as they are copied)

```bash
cp [-vr|--verbose --recursive] path/to/source_directory path/to/target_directory
```

### Copy multiple files at once to a directory

```bash
cp [-t|--target-directory] path/to/destination_directory path/to/file1 path/to/file2 ...
```

### Copy all files with a specific extension to another location, in interactive mode (prompts user before overwriting)

```bash
cp [-i|--interactive] *.ext path/to/target_directory
```

### Follow symbolic links before copying

```bash
cp [-L|--dereference] link path/to/target_directory
```

### Use the full path of source files, creating any missing intermediate directories when copying

```bash
cp --parents source/path/to/file path/to/target_file
```
