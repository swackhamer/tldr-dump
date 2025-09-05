# asdf

> Manage versions of different packages. More information: <https://asdf-vm.com/manage/commands.html>.

## Examples

### List all available plugins

```bash
asdf plugin list all
```

### Install a plugin

```bash
asdf plugin add name
```

### List all available versions for a package

```bash
asdf list all name
```

### Install a specific version of a package

```bash
asdf install name version
```

### Set global version for a package

```bash
asdf set -u name version
```

### Set local version for a package

```bash
asdf set name version
```

### See the current version used for a package

```bash
asdf current name
```
