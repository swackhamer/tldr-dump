# gdm

> The GNOME Display Manager (GDM) is a replacement for the X Display Manager (XDM). See also: `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`. More information: <https://manned.org/gdm>.

## Examples

### Run the GNOME Display Manager application

```bash
gdm
```

### Prevent `gdm` from being run as a daemon background process

```bash
gdm --nodaemon
```

### Disable `gdm` management of local console X servers for headless or remote environments

```bash
gdm --no-console
```

### Prevent sanitizing environment variables that start with `LD_`

```bash
gdm --preserve-ld-vars
```

### Display help

```bash
gdm --help
```

### Display version

```bash
gdm --version
```
