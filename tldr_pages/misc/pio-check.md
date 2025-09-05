# pio-check

> Perform a static analysis check on a PlatformIO project. More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

## Examples

### Perform a basic analysis check on the current project

```bash
pio check
```

### Perform a basic analysis check on a specific project

```bash
pio check [-d|--project-dir] project_dir
```

### Perform an analysis check for a specific environment

```bash
pio check [-e|--environment] environment
```

### Perform an analysis check and only report a specified defect severity type

```bash
pio check --severity low|medium|high
```

### Perform an analysis check and show detailed information when processing environments

```bash
pio check [-v|--verbose]
```
