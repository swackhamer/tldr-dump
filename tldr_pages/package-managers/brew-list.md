# brew-list

> List installed formulae/casks or their files. More information: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

## Examples

### List all installed formulae and casks

```bash
brew list
```

### List files belonging to an installed formula

```bash
brew list formula
```

### List artifacts of a cask

```bash
brew list cask
```

### List only formulae

```bash
brew list --formula
```

### List only casks

```bash
brew list --cask
```

### List only pinned formulae

```bash
brew list --pinned
```
