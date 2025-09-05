# chroot

> Run command or interactive shell with special root directory. More information: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

## Examples

### Run command as new root directory

```bash
sudo chroot path/to/new/root command
```

### Use a specific user and group

```bash
sudo chroot --userspec username_or_id:group_name_or_id
```
