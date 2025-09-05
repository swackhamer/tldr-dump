# liquidctl

> Control liquid coolers. More information: <https://github.com/liquidctl/liquidctl>.

## Examples

### List available devices

```bash
liquidctl list
```

### Initialize all supported devices

```bash
sudo liquidctl initialize all
```

### Print the status of available liquid coolers

```bash
liquidctl status
```

### Match a string in product name to pick a device and set its fan speed to 0% at 20°C, 50% at 50°C and 100% at 70°C

```bash
liquidctl --match string set fan speed 20 0 50 50 70 100
```
