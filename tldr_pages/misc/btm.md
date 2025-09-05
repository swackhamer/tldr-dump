# btm

> An alternative to `top`. Aims to be lightweight, cross-platform and more graphical than `top`. More information: <https://github.com/ClementTsang/bottom>.

## Examples

### Show the default layout (CPU, memory, temperatures, disk, network, and processes)

```bash
btm
```

### Enable basic mode, removing charts and condensing data (similar to `top`)

```bash
btm --basic
```

### Use big dots instead of small ones in charts

```bash
btm --dot_marker
```

### Show also battery charge and health status

```bash
btm --battery
```

### Refresh every 250 milliseconds and show the last 30 seconds in the charts

```bash
btm --rate 250 --default_time_value 30000
```
