# cupsd

> Server daemon for the CUPS print server. More information: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

## Examples

### Start `cupsd` in the background, aka. as a daemon

```bash
cupsd
```

### Start `cupsd` on the [f]oreground

```bash
cupsd -f
```

### [l]aunch `cupsd` on-demand (commonly used by `launchd` or `systemd`)

```bash
cupsd -l
```

### Start `cupsd` using the specified [`c`]`upsd.conf` configuration file

```bash
cupsd -c path/to/cupsd.conf
```

### Start `cupsd` using the specified `cups-file`[`s`]`.conf` configuration file

```bash
cupsd -s path/to/cups-files.conf
```

### [t]est the [`c`]`upsd.conf` configuration file for errors

```bash
cupsd -t -c path/to/cupsd.conf
```

### [t]est the `cups-file`[`s`]`.conf` configuration file for errors

```bash
cupsd -t -s path/to/cups-files.conf
```

### Display help

```bash
cupsd -h
```
