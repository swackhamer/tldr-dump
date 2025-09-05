# standard

> The JavaScript Standard Style tool for linting and fixing JavaScript code. More information: <https://standardjs.com>.

## Examples

### Lint all JavaScript source files in the current directory

```bash
standard
```

### Lint specific JavaScript file(s)

```bash
standard path/to/file1 path/to/file2 ...
```

### Apply automatic fixes during linting

```bash
standard --fix
```

### Declare any available global variables

```bash
standard --global variable
```

### Use a custom ESLint plugin when linting

```bash
standard --plugin plugin
```

### Use a custom JS parser when linting

```bash
standard --parser parser
```

### Use a custom ESLint environment when linting

```bash
standard --env environment
```
