# pip

> Python package manager. Some subcommands such as `install` have their own usage documentation. More information: <https://pip.pypa.io>.

## Examples

### Install a package (see `pip install` for more install examples)

```bash
pip install package
```

### Install a package to the user's directory instead of the system-wide default location

```bash
pip install --user package
```

### Upgrade a package

```bash
pip install [-U|--upgrade] package
```

### Uninstall a package

```bash
pip uninstall package
```

### Save installed packages to file

```bash
pip freeze > requirements.txt
```

### Show installed package info

```bash
pip show package
```

### Install packages from a file

```bash
pip install [-r|--requirement] requirements.txt
```
