# btop

> A resource monitor that shows information about the CPU, memory, disks, network and processes. A C++ version of `bpytop`. More information: <https://github.com/aristocratos/btop>.

## Examples

### Start `btop`

```bash
btop
```

### Start `btop` with the specified settings preset

```bash
btop [-p|--preset] 0..9
```

### Start `btop` in TTY mode using 16 colors and TTY-friendly graph symbols

```bash
btop [-t|--tty]
```

### Start `btop` in 256-color mode instead of 24-bit color mode

```bash
btop [-l|--low-color]
```

### Set the update rate to 500 milliseconds

```bash
btop [-u|--update] 500
```

### Exit `btop`

```bash
<q>
```

### Display help

```bash
btop [-h|--help]
```
