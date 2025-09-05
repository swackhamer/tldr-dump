# csslint

> Lint CSS code. More information: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

## Examples

### Lint a single CSS file

```bash
csslint file.css
```

### Lint multiple CSS files

```bash
csslint file1.css file2.css ...
```

### List all possible style rules

```bash
csslint --list-rules
```

### Treat certain rules as errors (which results in a non-zero exit code)

```bash
csslint --errors=errors,universal-selector,imports file.css
```

### Treat certain rules as warnings

```bash
csslint --warnings=box-sizing,selector-max,floats file.css
```

### Ignore specific rules

```bash
csslint --ignore=ids,rules-count,shorthand file.css
```
