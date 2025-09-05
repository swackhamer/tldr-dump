# distccd

> Server daemon for the distcc distributed compiler. More information: <https://distcc.github.io>.

## Examples

### Start a daemon with the default settings

```bash
distccd --daemon
```

### Start a daemon, accepting connections from IPv4 private network ranges

```bash
distccd --daemon --allow-private
```

### Start a daemon, accepting connections from a specific network address or address range

```bash
distccd --daemon [-a|--allow] ip_address|network_prefix
```

### Start a daemon with a lowered priority that can run a maximum of 4 tasks at a time

```bash
distccd --daemon [-j|--jobs] 4 [-N|--nice] 5
```

### Start a daemon and register it via mDNS/DNS-SD (Zeroconf)

```bash
distccd --daemon --zeroconf
```
