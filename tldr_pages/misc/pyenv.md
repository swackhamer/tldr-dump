# pyenv

> Switch between multiple versions of Python easily. See also: `asdf`. More information: <https://github.com/pyenv/pyenv>.

## Examples

### List all available commands

```bash
pyenv commands
```

### List all Python versions under the `${PYENV_ROOT}/versions` directory

```bash
pyenv versions
```

### List all Python versions that can be installed from upstream

```bash
pyenv install --list
```

### Install a Python version under the `${PYENV_ROOT}/versions` directory

```bash
pyenv install 2.7.10
```

### Uninstall a Python version under the `${PYENV_ROOT}/versions` directory

```bash
pyenv uninstall 2.7.10
```

### Set Python version to be used globally in the current machine

```bash
pyenv global 2.7.10
```

### Set Python version to be used in the current directory and all directories below it

```bash
pyenv local 2.7.10
```
