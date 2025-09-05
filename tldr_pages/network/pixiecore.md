# pixiecore

> Manage the network booting of machines. More information: <https://github.com/danderson/netboot/tree/master/pixiecore>.

## Examples

### Start a PXE boot server which provides a `netboot.xyz` boot image

```bash
pixiecore quick xyz --dhcp-no-bind
```

### Start a new PXE boot server which provides an Ubuntu boot image

```bash
pixiecore quick ubuntu --dhcp-no-bind
```

### List all available boot images for quick mode

```bash
pixiecore quick --help
```
