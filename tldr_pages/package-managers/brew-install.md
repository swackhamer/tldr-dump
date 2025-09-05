# brew-install

> Install a Homebrew formula or cask. More information: <https://docs.brew.sh/Manpage#install-options-formulacask->.

## Examples

### Install a formula/cask

```bash
brew install formula|cask
```

### Build and install a formula from source (dependencies will still be installed from bottles)

```bash
brew install [-s|--build-from-source] formula
```

### Download the manifest, print what would be installed but don't actually install anything

```bash
brew install [-n|--dry-run] formula|cask
```
