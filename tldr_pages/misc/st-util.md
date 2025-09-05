# st-util

> Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller. More information: <https://github.com/texane/stlink>.

## Examples

### Run GDB server on port 4500

```bash
st-util [-p|--listen_port] 4500
```

### Connect to GDB server within `gdb`

```bash
target extended-remote localhost:4500
```

### Write firmware to device

```bash
load firmware.elf
```
