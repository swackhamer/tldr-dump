# steam

> Video game platform by Valve. More information: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

## Examples

### Launch Steam, printing debug messages to `stdout`

```bash
steam
```

### Launch Steam and enable its in-app debug console tab

```bash
steam -console
```

### Enable and open the Steam console tab in a running Steam instance

```bash
steam steam://open/console
```

### Log into Steam with the specified credentials

```bash
steam -login username password
```

### Launch Steam in Big Picture Mode

```bash
steam -tenfoot
```

### Exit Steam

```bash
steam -shutdown
```
