# sntpd

> An SNTP server. It should not be invoked manually. More information: <https://keith.github.io/xcode-man-pages/sntpd.8.html>.

## Examples

### Start the daemon

```bash
sntpd
```

### Overwrite existing state with the local clock (stratum 1), for running a master/primary server, without synchronizing with another (higher stratum) server

```bash
sntpd -L
```

### Use a custom file for the SNTP state

```bash
sntpd -z path/to/state.bin
```
