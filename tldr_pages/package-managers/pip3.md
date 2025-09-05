# pip3

> Python package manager. More information: <https://pip.pypa.io>.

## Examples

### Install a package

```bash
pip3 install package
```

### Install a specific version of a package

```bash
pip3 install package==version
```

### Upgrade a package

```bash
pip3 install [-U|--upgrade] package
```

### Uninstall a package

```bash
pip3 uninstall package
```

### Save the list of installed packages to a file

```bash
pip3 freeze > requirements.txt
```

### Install packages from a file

```bash
pip3 install [-r|--requirement] requirements.txt
```

### Show installed package info

```bash
pip3 show package
```
