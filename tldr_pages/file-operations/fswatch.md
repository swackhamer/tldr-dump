# fswatch

> A cross-platform file change monitor. More information: <https://emcrisostomo.github.io/fswatch>.

## Examples

### Run a Bash command on file creation, update or deletion

```bash
fswatch path/to/file | xargs [-n|--max-args] 1 bash_command
```

### Watch one or more files and/or directories

```bash
fswatch path/to/file path/to/directory path/to/another_directory/**/*.js | xargs [-n|--max-args] 1 bash_command
```

### Print the absolute paths of the changed files

```bash
fswatch path/to/directory | xargs [-n|--max-args] 1 -I _ echo _
```

### Filter by event type

```bash
fswatch --event Updated|Removed|Created|... path/to/directory | xargs [-n|--max-args] 1 bash_command
```
