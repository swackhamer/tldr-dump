# ruff-check

> An extremely fast Python linter. `check` is the default command - it can be omitted everywhere. If no files or directories are specified, the current working directory is used by default. More information: <https://docs.astral.sh/ruff/linter>.

## Examples

### Run the linter on the given files or directories

```bash
ruff check path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Apply the suggested fixes, modifying the files in-place

```bash
ruff check --fix
```

### Run the linter and re-lint on change

```bash
ruff check --watch
```

### Only enable the specified rules (or all rules), ignoring the configuration file

```bash
ruff check --select ALL|rule_code1,rule_code2,...
```

### Additionally enable the specified rules

```bash
ruff check --extend-select rule_code1,rule_code2,...
```

### Disable the specified rules

```bash
ruff check --ignore rule_code1,rule_code2,...
```

### Ignore all existing violations of a rule by adding `# noqa` directives to all lines that violate it

```bash
ruff check --select rule_code --add-noqa
```
