# avrdude

> Driver program for Atmel AVR microcontrollers programming. More information: <https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

## Examples

### [r]ead the flash ROM of a AVR microcontroller with a specific [p]art ID

```bash
avrdude -p part_no -c programmer_id -U flash:r:file.hex:i
```

### [w]rite to the flash ROM AVR microcontroller

```bash
avrdude -p part_no -c programmer -U flash:w:file.hex
```

### List available AVR devices

```bash
avrdude -p \?
```

### List available AVR programmers

```bash
avrdude -c \?
```
