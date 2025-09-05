# gh-codespace

> Connect and manage your codespaces in GitHub. More information: <https://cli.github.com/manual/gh_codespace>.

## Examples

### Create a codespace in GitHub interactively

```bash
gh codespace create
```

### List all available codespaces

```bash
gh codespace list
```

### Connect to a codespace via SSH interactively

```bash
gh codespace ssh
```

### Transfer a specific file to a codespace interactively

```bash
gh codespace cp path/to/source_file remote:path/to/remote_file
```

### List the ports of a codespace interactively

```bash
gh codespace ports
```

### Display the logs from a codespace interactively

```bash
gh codespace logs
```

### Delete a codespace interactively

```bash
gh codespace delete
```

### Display help for a subcommand

```bash
gh codespace code|cp|create|delete|edit|... --help
```
