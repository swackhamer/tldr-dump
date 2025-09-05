# pydocstyle

> Statically check Python scripts for compliance with Python docstring conventions. More information: <https://www.pydocstyle.org/en/latest/>.

## Examples

### Analyze a Python script or all the Python scripts in a specific directory

```bash
pydocstyle file.py|path/to/directory
```

### Show an explanation of each error

```bash
pydocstyle [-e|--explain] file.py|path/to/directory
```

### Show debug information

```bash
pydocstyle [-d|--debug] file.py|path/to/directory
```

### Display the total number of errors

```bash
pydocstyle --count file.py|path/to/directory
```

### Use a specific configuration file

```bash
pydocstyle --config path/to/config_file file.py|path/to/directory
```

### Ignore one or more errors

```bash
pydocstyle --ignore D101,D2,D107,... file.py|path/to/directory
```

### Check for errors from a specific convention

```bash
pydocstyle --convention pep257|numpy|google file.py|path/to/directory
```
