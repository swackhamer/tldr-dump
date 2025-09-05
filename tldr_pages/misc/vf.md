# vf

> VirtualFish is a fish shell tool for managing Python virtual environments. More information: <https://virtualfish.readthedocs.io/en/latest/>.

## Examples

### Create a virtual environment

```bash
vf new virtualenv_name
```

### Create a virtual environment for a specific Python version

```bash
vf new --python /usr/local/bin/python3.8 virtualenv_name
```

### Activate and use the specified virtual environment

```bash
vf activate virtualenv_name
```

### Connect the current virtualenv to the current directory, so that it is activated automatically as soon as you enter it (and deactivated as soon as you leave)

```bash
vf connect
```

### Deactivate the current virtual environment

```bash
vf deactivate
```

### List all virtual environments

```bash
vf ls
```

### Remove a virtual environment

```bash
vf rm virtualenv_name
```

### Display help

```bash
vf help
```
