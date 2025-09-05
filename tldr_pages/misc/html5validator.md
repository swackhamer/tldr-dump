# html5validator

> Validate HTML5. More information: <https://github.com/svenkreiss/html5validator>.

## Examples

### Validate a specific file

```bash
html5validator path/to/file
```

### Validate all HTML files in a specific directory

```bash
html5validator --root path/to/directory
```

### Show warnings as well as errors

```bash
html5validator --show-warnings path/to/file
```

### Match multiple files using a glob pattern

```bash
html5validator --root path/to/directory --match "*.html *.php"
```

### Ignore specific directory names

```bash
html5validator --root path/to/directory --blacklist "node_modules vendor"
```

### Output the results in a specific format

```bash
html5validator --format gnu|xml|json|text path/to/file
```

### Output the log at a specific verbosity level

```bash
html5validator --root path/to/directory --log debug|info|warning
```
