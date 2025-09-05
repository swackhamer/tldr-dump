# busybox

> A collection of small system utilities in a single executable. Executing `busybox` via a symlink is equivalent to running `busybox symlink_name`. Linux distributions that use BusyBox will usually provide symlinks for all programs. More information: <https://www.busybox.net/downloads/BusyBox.html>.

## Examples

### Execute a BusyBox function

```bash
busybox ls|rm|mkdir|cat|... args
```

### Display help and a list of functions

```bash
busybox --help
```
