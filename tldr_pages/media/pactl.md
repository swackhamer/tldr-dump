# pactl

> Control a running PulseAudio sound server. More information: <https://manned.org/pactl>.

## Examples

### Show information about the sound server

```bash
pactl info
```

### List all sinks (or other types - sinks are outputs and sink-inputs are active audio streams)

```bash
pactl list sinks short
```

### Change the default sink (output) to 1 (the number can be retrieved via the `list` subcommand)

```bash
pactl set-default-sink 1
```

### Move sink-input 627 to sink 1

```bash
pactl move-sink-input 627 1
```

### Set the volume of sink 1 to 75%

```bash
pactl set-sink-volume 1 0.75
```

### Toggle mute on the default sink (using the special name `@DEFAULT_SINK@`)

```bash
pactl set-sink-mute @DEFAULT_SINK@ toggle
```
