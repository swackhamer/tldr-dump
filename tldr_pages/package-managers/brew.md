# brew

> Homebrew - a package manager for macOS and Linux. Some subcommands such as `install` have their own usage documentation. More information: <https://docs.brew.sh/Manpage>.

## Examples

### Install the latest stable version of a formula or cask (use `--devel` for development versions)

```bash
brew install formula
```

### List all installed formulae and casks

```bash
brew list
```

### Upgrade an installed formula or cask (if none is given, all installed formulae/casks are upgraded)

```bash
brew upgrade formula
```

### Fetch the newest version of Homebrew and of all formulae and casks from the Homebrew source repository

```bash
brew update
```

### Show formulae and casks that have a more recent version available

```bash
brew outdated
```

### Search for available formulae (i.e. packages) and casks (i.e. native macOS `.app` packages)

```bash
brew search text
```

### Display information about a formula or a cask (version, installation path, dependencies, etc.)

```bash
brew info formula
```

### Check the local Homebrew installation for potential problems

```bash
brew doctor
```
