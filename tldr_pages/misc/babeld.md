# babeld

> Routing daemon for Babel which uses firewall-style filters. More information: <https://www.irif.fr/~jch/software/babel/babeld.html>.

## Examples

### Start the daemon with one or more [c]onfiguration files (read in order)

```bash
babeld -c path/to/ports.conf -c path/to/filters.conf -c path/to/interfaces.conf
```

### [D]eamonize after startup

```bash
babeld -D
```

### Specify a [C]onfiguration command

```bash
babeld -C 'redistribute metric 256'
```

### Specify on which interfaces to operate

```bash
babeld eth0 eth1 wlan0
```
