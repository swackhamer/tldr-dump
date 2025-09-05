# fping

> A more powerful ping which can ping multiple hosts. More information: <https://fping.org>.

## Examples

### List the status of all hosts within a range

```bash
fping 192.168.1.{1..254}
```

### List alive hosts within a subnet generated from a netmask

```bash
fping [-a|--alive] [-g|--generate] 192.168.1.0/24
```

### List alive hosts within a subnet generated from an IP range and prune per-probe results

```bash
fping [-q|--quiet] [-a|--alive] [-g|--generate] 192.168.1.1 192.168.1.254
```

### List unreachable hosts within a subnet generated from a netmask

```bash
fping [-u|--unreach] [-g|--generate] 192.168.1.0/24
```
