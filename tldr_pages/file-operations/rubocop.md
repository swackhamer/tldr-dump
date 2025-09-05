# rubocop

> Lint Ruby files. More information: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

## Examples

### Check all files in the current directory (including subdirectories)

```bash
rubocop
```

### Check one or more specific files or directories

```bash
rubocop path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Write output to file

```bash
rubocop --out path/to/file
```

### View list of cops (linter rules)

```bash
rubocop --show-cops
```

### Exclude a cop

```bash
rubocop --except cop1 cop2 ...
```

### Run only specified cops

```bash
rubocop --only cop1 cop2 ...
```

### Auto-correct files (experimental)

```bash
rubocop --auto-correct
```
