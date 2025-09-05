# pio-update

> Update installed PlatformIO Core packages, development platforms and global libraries. See also: `pio platform update`, `pio lib update`. More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_update.html>.

## Examples

### Perform a full update of all packages, development platforms and global libraries

```bash
pio update
```

### Update core packages only (skips platforms and libraries)

```bash
pio update --core-packages
```

### Check for new versions of packages, platforms and libraries but do not actually update them

```bash
pio update --dry-run
```
