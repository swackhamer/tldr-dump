# gimp

> GNU image manipulation program. See also: `krita`. More information: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

## Examples

### Start GIMP

```bash
gimp
```

### Open specific files

```bash
gimp path/to/image1 path/to/image2 ...
```

### Open specific files in a new window

```bash
gimp --new-instance path/to/image1 path/to/image2 ...
```

### Start without a splash screen

```bash
gimp --no-splash
```

### Print errors and warnings to the console instead of showing them in a dialog box

```bash
gimp --console-messages
```

### Enable debugging signal handlers

```bash
gimp --debug-handlers
```
