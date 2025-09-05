# sfdk-config

> Configures sfdk. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/command.config.adoc>.

## Examples

### Show configuration in all scopes

```bash
sfdk config --show
```

### Set a configuration value

```bash
sfdk config name=value
```

### Mask an option as empty

```bash
sfdk config name=
```

### Mask an option as empty without pushing it at the inner scope

```bash
sfdk config name
```

### Clear option value

```bash
sfdk --drop name
```

### Run subcommand in specified scope (`global`, `session` or `command`)

```bash
sfdk config --scope subcommand
```
