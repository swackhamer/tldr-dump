# pio-system

> Miscellaneous system commands for PlatformIO. More information: <https://docs.platformio.org/en/latest/core/userguide/system/>.

## Examples

### Install shell completion for the current shell (supports Bash, fish, Zsh and PowerShell)

```bash
pio system completion install
```

### Uninstall shell completion for the current shell

```bash
pio system completion uninstall
```

### Display system-wide PlatformIO information

```bash
pio system info
```

### Remove unused PlatformIO data

```bash
pio system prune
```

### Remove only cached data

```bash
pio system prune --cache
```

### List unused PlatformIO data that would be removed but do not actually remove it

```bash
pio system prune --dry-run
```
