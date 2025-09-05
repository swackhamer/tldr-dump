# atoum

> A simple, modern and intuitive unit testing framework for PHP. More information: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

## Examples

### Initialize a configuration file

```bash
atoum --init
```

### Run all tests

```bash
atoum
```

### Run tests using the specified configuration file

```bash
atoum [-c|--configuration] path/to/file
```

### Run a specific test file

```bash
atoum [-f|--files] path/to/file
```

### Run a specific directory of tests

```bash
atoum [-d|--directories] path/to/directory
```

### Run all tests under a specific namespace

```bash
atoum [-ns|--namespaces] namespace
```

### Run all tests with a specific tag

```bash
atoum [-t|--tags] tag
```

### Load a custom bootstrap file before running tests

```bash
atoum [-bf|--bootstrap-file] path/to/file
```
