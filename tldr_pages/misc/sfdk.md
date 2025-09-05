# sfdk

> The command line frontend of the Sailfish SDK. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/module.adoc>.

## Examples

### Execute a subcommand

```bash
sfdk subcommand
```

### Execute a subcommand on a custom working directory

```bash
git -C path/to/directory subcommand
```

### Execute a subcommand with a given configuration set

```bash
git -c 'name=value' subcommand
```

### Display help

```bash
sfdk [-h|--help]
```

### Display help for specific topic (`building`, `testing`, `maintaining`, `ide`, `all`)

```bash
sfdk --help-topic
```

### Display version

```bash
sfdk --version
```
