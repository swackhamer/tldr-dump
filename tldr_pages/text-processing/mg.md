# mg

> A small, fast, and portable text editor based on `emacs`. More information: <https://manned.org/mg>.

## Examples

### Open a file for editing

```bash
mg path/to/file
```

### Open a file at a specified line number

```bash
mg +line_number path/to/file
```

### Open files in a read-only mode

```bash
mg -R path/to/file1 path/to/file2 ...
```

### Disable `~` backup files while editing

```bash
mg -n path/to/file
```
