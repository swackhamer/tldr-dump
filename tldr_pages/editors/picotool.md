# picotool

> Manage Raspberry Pi Pico boards. More information: <https://github.com/raspberrypi/picotool>.

## Examples

### Display information about the currently loaded program on a Pico

```bash
picotool info
```

### Load a binary onto a Pico

```bash
picotool load path/to/binary
```

### Convert an ELF or BIN file to UF2

```bash
picotool uf2 convert path/to/elf_or_bin path/to/output
```

### Reboot a Pico

```bash
picotool reboot
```

### List all known registers

```bash
picotool otp list
```

### Display version

```bash
picotool version
```

### Display help

```bash
picotool help
```
