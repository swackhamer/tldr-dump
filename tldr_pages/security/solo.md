# solo

> Interact with Solo hardware security keys. More information: <https://github.com/solokeys/solo-python>.

## Examples

### List connected Solos

```bash
solo ls
```

### Update the currently connected Solo's firmware to the latest version

```bash
solo key update
```

### Blink the LED of a specific Solo

```bash
solo key wink --serial serial_number
```

### Generate random bytes using the currently connected Solo's secure random number generator

```bash
solo key rng raw
```

### Monitor the serial output of a Solo

```bash
solo monitor path/to/serial_port
```
