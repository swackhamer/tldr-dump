# ifdata

> Display information about a network interface. More information: <https://manned.org/ifdata>.

## Examples

### Display the whole configuration of the specified interface

```bash
ifdata -p eth0
```

### Indicate the [e]xistence of the specified interface via the exit code

```bash
ifdata -e eth0
```

### Display the IPv4 [a]dress and the [n]etmask of the specified interface

```bash
ifdata -pa -pn eth0
```

### Display the [N]etwork adress, the [b]roadcast adress, and the MTU of the specified interface

```bash
ifdata -pN -pb -pm eth0
```

### Display help

```bash
ifdata
```
