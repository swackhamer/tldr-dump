# lsyncd

> Watch files and directories and run `rsync` when they change. It is often used to keep two directories on separate systems in sync, ensuring that changes made in one directory are immediately mirrored to the other. More information: <https://github.com/lsyncd/lsyncd>.

## Examples

### Watch the source for changes and run `rsync` to synchronize files to the destination on every change

```bash
lsyncd -rsync path/to/source host::share_name
```

### Use SSH instead of `rsyncd` shares

```bash
lsyncd -rsyncssh path/to/source host path/to/destination
```
