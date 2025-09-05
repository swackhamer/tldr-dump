# pip-freeze

> List installed packages in requirements format. More information: <https://pip.pypa.io/en/stable/cli/pip_freeze>.

## Examples

### List installed packages

```bash
pip freeze
```

### List installed packages and write it to the `requirements.txt` file

```bash
pip freeze > requirements.txt
```

### List installed packages in a virtual environment, excluding globally installed packages

```bash
pip freeze [-l|--local] > requirements.txt
```

### List installed packages in the user-site

```bash
pip freeze --user > requirements.txt
```

### List all packages, including `pip`, `distribute`, `setuptools`, and `wheel` (they are skipped by default)

```bash
pip freeze --all > requirements.txt
```
