# trawl

> Print out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata. More information: <https://github.com/robphoenix/trawl>.

## Examples

### Show column names

```bash
trawl -n
```

### Filter interface names using a case-insensitive `regex`

```bash
trawl -f wi
```

### List available interfaces

```bash
trawl -i
```

### Include the loopback interface

```bash
trawl -l
```
