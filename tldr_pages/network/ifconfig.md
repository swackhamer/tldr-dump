# ifconfig

> Network Interface Configurator. More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

## Examples

### View network settings of an interface

```bash
ifconfig interface_name
```

### Display details of all interfaces, including disabled interfaces

```bash
ifconfig -a
```

### Disable an interface

```bash
ifconfig interface_name down
```

### Enable an interface

```bash
ifconfig interface_name up
```

### Assign an IP address to an interface

```bash
ifconfig interface_name ip_address
```
