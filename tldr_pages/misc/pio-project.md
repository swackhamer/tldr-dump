# pio-project

> Manage PlatformIO projects. More information: <https://docs.platformio.org/en/latest/core/userguide/project/>.

## Examples

### Initialize a new PlatformIO project

```bash
pio project init
```

### Initialize a new PlatformIO project in a specific directory

```bash
pio project init [-d|--project-dir] path/to/project_directory
```

### Initialize a new PlatformIO project, specifying a board ID

```bash
pio project init [-b|--board] ATmega328P|uno|...
```

### Initialize a new PlatformIO based project, specifying one or more project options

```bash
pio project init [-O|--project-option] "option=value" [-O|--project-option] "option=value"
```

### Print the configuration of a project

```bash
pio project config
```
