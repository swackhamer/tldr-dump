# goku

> Manage Karabiner configuration. More information: <https://github.com/yqrashawn/GokuRakuJoudo>.

## Examples

### Generate `karabiner.json` using the default configuration

```bash
goku
```

### Generate `karabiner.json` using the specific `config.edn` file

```bash
goku --config path/to/config.edn
```

### Dry run the new configuration into `stdout` instead of updating `karabiner.json`

```bash
goku --dry-run
```

### Dry run the whole configuration into `stdout` instead of updating `karabiner.json`

```bash
goku --dry-run-all
```

### Display help

```bash
goku --help
```

### Display version

```bash
goku --version
```
