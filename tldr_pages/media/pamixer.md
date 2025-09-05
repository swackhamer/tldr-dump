# pamixer

> A simple command-line mixer for PulseAudio. More information: <https://github.com/cdemoulins/pamixer#installation>.

## Examples

### List all sinks and sources with their corresponding IDs

```bash
pamixer --list-sinks --list-sources
```

### Set the volume to 75% on the default sink

```bash
pamixer --set-volume 75
```

### Toggle mute on a sink other than the default

```bash
pamixer --toggle-mute --sink ID
```

### Increase the volume on default sink by 5%

```bash
pamixer [-i|--increase] 5
```

### Decrease the volume on a source by 5%

```bash
pamixer [-d|--decrease] 5 --source ID
```

### Use the allow boost option to increase, decrease, or set the volume above 100%

```bash
pamixer --set-volume 105 --allow-boost
```

### Mute the default sink (use `--unmute` instead to unmute)

```bash
pamixer [-m|--mute]
```
