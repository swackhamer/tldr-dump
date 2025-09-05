# upt

> Unified interface for managing packages across various operating systems, like Windows, many Linux distributions, macOS, FreeBSD and even Haiku. It requires the native OS package manager to be installed. See also: `flatpak`, `brew`, `scoop`, `apt`, `dnf`. More information: <https://github.com/sigoden/upt>.

## Examples

### Update the list of available packages

```bash
upt update
```

### Search for a given package

```bash
upt search search_term
```

### Show information for a package

```bash
upt info package
```

### Install a given package

```bash
upt install package
```

### Remove a given package

```bash
upt remove|uninstall package
```

### Upgrade all installed packages

```bash
upt upgrade
```

### Upgrade a given package

```bash
upt upgrade package
```

### List installed packages

```bash
upt list
```
