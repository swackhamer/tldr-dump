# virtualenvwrapper

> Group of simple wrapper commands for Python's `virtualenv` tool. More information: <https://virtualenvwrapper.readthedocs.org>.

## Examples

### Create a new Python `virtualenv` in `$WORKON_HOME`

```bash
mkvirtualenv virtualenv_name
```

### Create a `virtualenv` for a specific Python version

```bash
mkvirtualenv --python /usr/local/bin/python3.8 virtualenv_name
```

### Activate or use a different `virtualenv`

```bash
workon virtualenv_name
```

### Stop the `virtualenv`

```bash
deactivate
```

### List all virtual environments

```bash
lsvirtualenv
```

### Remove a `virtualenv`

```bash
rmvirtualenv virtualenv_name
```

### Get summary of all virtualenvwrapper commands

```bash
virtualenvwrapper
```
