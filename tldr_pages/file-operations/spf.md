# spf

> The superfile – Modern terminal file manager. More information: <https://github.com/yorukot/superfile>.

## Examples

### Launch `spf` with a specific path

```bash
spf path/to/directory
```

### Launch `spf` with multiple paths

```bash
spf path/to/directory1 path/to/directory2 ...
```

### Fix hotkey settings by appending missing keys

```bash
spf [--fh|--fix-hotkeys]
```

### Fix the configuration file by appending missing entries

```bash
spf [--fch|--fix-config-file]
```

### Use specific configuration and hotkey files

```bash
spf [-c|--config-file] path/to/config.toml [--hf|--hotkey-file] path/to/hotkey.toml
```

### Write the path of the first selected file to this file and exit

```bash
spf [--cf|--chooser-file] tmp/chooser-result
```

### Show internal configuration and data directory paths

```bash
spf [pl|path-list]
```
