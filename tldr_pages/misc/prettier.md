# prettier

> An opinionated code formatter for JavaScript, JSON, CSS, YAML, and more. More information: <https://prettier.io/docs/cli>.

## Examples

### Format a file and print the result to `stdout`

```bash
prettier path/to/file
```

### Check if a specific file has been formatted

```bash
prettier --check path/to/file
```

### Run with a specific configuration file

```bash
prettier --config path/to/config_file path/to/file
```

### Format a file or directory, replacing the original

```bash
prettier --write path/to/file_or_directory
```

### Format files or directories recursively using single quotes and no trailing commas

```bash
prettier --single-quote --trailing-comma none --write path/to/file_or_directory
```

### Format JavaScript and TypeScript files recursively, replacing the original

```bash
prettier --write "**/*.{js,jsx,ts,tsx}"
```
