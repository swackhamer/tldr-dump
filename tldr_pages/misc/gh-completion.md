# gh-completion

> Generate shell completion scripts for GitHub CLI commands. More information: <https://cli.github.com/manual/gh_completion>.

## Examples

### Print a completion script

```bash
gh completion [-s|--shell] bash|zsh|fish|powershell
```

### Append the `gh` completion script to `~/.bashrc`

```bash
gh completion [-s|--shell] bash >> ~/.bashrc
```

### Append the `gh` completion script to `~/.zshrc`

```bash
gh completion [-s|--shell] zsh >> ~/.zshrc
```

### Display the subcommand help

```bash
gh completion
```
