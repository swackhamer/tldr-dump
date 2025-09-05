# sysctl

> Access kernel state information. More information: <https://keith.github.io/xcode-man-pages/sysctl.8.html>.

## Examples

### Show all available variables and their values

```bash
sysctl -a
```

### Show Apple model identifier

```bash
sysctl -n hw.model
```

### Show CPU model

```bash
sysctl -n machdep.cpu.brand_string
```

### Show available CPU features (MMX, SSE, SSE2, SSE3, AES, etc)

```bash
sysctl -n machdep.cpu.features
```

### Set a changeable kernel state variable

```bash
sysctl -w section.tunable=value
```
