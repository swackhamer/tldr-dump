# resolvconf

> Manage nameserver information. Acts as an intermediary between programs that supply nameserver information and applications that use this information. This page documents Debian's implementation of `resolvconf`. More information: <https://manned.org/resolvconf.8>.

## Examples

### Add or override the IFACE.PROG record and run the update scripts if updating is enabled

```bash
resolvconf -a IFACE.PROG
```

### Delete the IFACE.PROG record and run the update scripts if updating is enabled

```bash
resolvconf -d IFACR.PROG
```

### Just run the update scripts if updating is enabled

```bash
resolvconf -u
```

### Set the flag indicating whether `resolvconf` should run update scripts when invoked with `-a`, `-d` or `-u`

```bash
resolvconf --enable-updates
```

### Clear the flag indicating whether to run updates

```bash
resolvconf --disable-updates
```

### Check whether updates are enabled

```bash
resolvconf --updates-are-enabled
```
