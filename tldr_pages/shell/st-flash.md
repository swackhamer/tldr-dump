# st-flash

> Flash binary files to STM32 ARM Cortex microcontrollers. More information: <https://manned.org/st-flash>.

## Examples

### Read 4096 bytes from the device starting from 0x8000000

```bash
st-flash read firmware.bin 0x8000000 4096
```

### Write firmware to device starting from 0x8000000

```bash
st-flash write firmware.bin 0x8000000
```

### Erase firmware from device

```bash
st-flash erase
```
