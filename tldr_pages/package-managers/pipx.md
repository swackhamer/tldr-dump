# pipx

> Install and run Python applications in isolated environments. More information: <https://github.com/pypa/pipx>.

## Examples

### Run an app in a temporary virtual environment

```bash
pipx run pycowsay moo
```

### Install a package in a virtual environment and add entry points to path

```bash
pipx install package
```

### List installed packages

```bash
pipx list
```

### Run an app in a temporary virtual environment with a package name different from the executable

```bash
pipx run --spec httpx-cli httpx http://www.github.com
```

### Inject dependencies into an existing virtual environment

```bash
pipx inject package dependency1 dependency2 ...
```

### Install a package in a virtual environment with pip arguments

```bash
pipx install --pip-args='pip-args' package
```

### Upgrade/reinstall/uninstall all installed packages

```bash
pipx upgrade-all|uninstall-all|reinstall-all
```
