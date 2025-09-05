# pio-run

> Run PlatformIO project targets. More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

## Examples

### List all available project targets

```bash
pio run --list-targets
```

### List all available project targets of a specific environment

```bash
pio run --list-targets [-e|--environment] environment
```

### Run all targets

```bash
pio run
```

### Run all targets of specified environments

```bash
pio run [-e|--environment] environment1 [-e|--environment] environment2
```

### Run specified targets

```bash
pio run [-t|--target] target1 [-t|--target] target2
```

### Run the targets of a specified configuration file

```bash
pio run [-c|--project-conf] path/to/platformio.ini
```
