# parallel-lint

> Check the syntax of PHP files in parallel. More information: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

## Examples

### Lint a specific directory

```bash
parallel-lint path/to/directory
```

### Lint a directory using the specified number of parallel processes

```bash
parallel-lint -j processes path/to/directory
```

### Lint a directory, excluding the specified directory

```bash
parallel-lint --exclude path/to/excluded_directory path/to/directory
```

### Lint a directory of files using a comma-separated list of extension(s)

```bash
parallel-lint -e php,html,phpt path/to/directory
```

### Lint a directory and output the results as JSON

```bash
parallel-lint --json path/to/directory
```

### Lint a directory and show Git Blame results for rows containing errors

```bash
parallel-lint --blame path/to/directory
```
