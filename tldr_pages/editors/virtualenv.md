# virtualenv

> Create virtual isolated Python environments. More information: <https://virtualenv.pypa.io/en/latest/cli_interface.html>.

## Examples

### Create a new environment

```bash
virtualenv path/to/venv
```

### Customize the prompt prefix

```bash
virtualenv --prompt prompt_prefix path/to/venv
```

### Use a different version of Python with virtualenv

```bash
virtualenv [-p|--python] path/to/pythonbin path/to/venv
```

### Start (select) the environment

```bash
source path/to/venv/bin/activate
```

### Stop the environment

```bash
deactivate
```
