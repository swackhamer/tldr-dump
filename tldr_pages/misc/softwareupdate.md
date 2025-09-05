# softwareupdate

> Update macOS App Store apps. More information: <https://keith.github.io/xcode-man-pages/softwareupdate.8.html>.

## Examples

### List all available updates

```bash
softwareupdate --list
```

### Download and install all updates

```bash
softwareupdate --install --all
```

### Download and install all [r]ecommended updates

```bash
softwareupdate --install --recommended
```

### Download and install a specific app

```bash
softwareupdate --install update_name
```
