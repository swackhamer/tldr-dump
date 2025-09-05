# help2man

> Produce simple man pages from an executable's `--help` and `--version` output. More information: <https://www.gnu.org/software/help2man/#Invoking-help2man>.

## Examples

### Generate a man page for an executable

```bash
help2man executable
```

### Specify the "name" paragraph in the man page

```bash
help2man executable [-n|--name] name
```

### Specify the section for the man page (defaults to 1)

```bash
help2man executable [-s|--section] section
```

### Output to a file instead of `stdout`

```bash
help2man executable [-o|--output] path/to/file
```

### Display help

```bash
help2man --help
```
