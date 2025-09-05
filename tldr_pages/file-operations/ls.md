# ls

> List directory contents. More information: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

## Examples

### List files one per line

```bash
ls -1
```

### List all files, including hidden files

```bash
ls [-a|--all]
```

### List files with a trailing symbol to indicate file type (directory/, symbolic_link@, executable*, ...)

```bash
ls [-F|--classify]
```

### List all files in [l]ong format (permissions, ownership, size, and modification date)

```bash
ls [-la|-l --all]
```

### List files in [l]ong format with size displayed using human-readable units (KiB, MiB, GiB)

```bash
ls [-lh|-l --human-readable]
```

### List files in [l]ong format, sorted by [S]ize (descending) recursively

```bash
ls [-lSR|-lS --recursive]
```

### List files in [l]ong format, sorted by [t]ime the file was modified and in reverse order (oldest first)

```bash
ls [-ltr|-lt --reverse]
```

### Only list directories

```bash
ls [-d|--directory] */
```
