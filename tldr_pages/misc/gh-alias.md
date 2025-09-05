# gh-alias

> Manage GitHub CLI command aliases. More information: <https://cli.github.com/manual/gh_alias>.

## Examples

### List all the aliases `gh` is configured to use

```bash
gh alias list
```

### Create a `gh` subcommand alias

```bash
gh alias set pv 'pr view'
```

### Set a shell command as a `gh` subcommand

```bash
gh alias set [-s|--shell] alias_name command
```

### Delete a command shortcut

```bash
gh alias delete alias_name
```

### Display the subcommand help

```bash
gh alias
```
