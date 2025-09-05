# pip-install

> Install Python packages. More information: <https://pip.pypa.io>.

## Examples

### Install a package

```bash
pip install package
```

### Install a specific version of a package

```bash
pip install package==version
```

### Install packages listed in a file

```bash
pip install [-r|--requirement] path/to/requirements.txt
```

### Install packages from an URL or local file archive (.tar.gz | .whl)

```bash
pip install [-f|--find-links] url|path/to/file
```

### Install the local package in the current directory in develop (editable) mode

```bash
pip install [-e|--editable] .
```
