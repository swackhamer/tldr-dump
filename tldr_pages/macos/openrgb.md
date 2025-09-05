# openrgb

> Control RGB lighting. More information: <https://gitlab.com/OpenRGBDevelopers/OpenRGB-Wiki/-/blob/stable/User-Documentation/Using-OpenRGB.md>.

## Examples

### Start the OpenRGB GUI

```bash
openrgb
```

### List devices supported by OpenRGB

```bash
openrgb --noautoconnect [-l|--list-devices]
```

### Set the mode and color of a device

```bash
openrgb [-m|--mode] off|static|breathing|rainbow|flashing|... [-c|--color] random|red|00AAFF|...
```

### Display help

```bash
openrgb [-h|--help]
```
