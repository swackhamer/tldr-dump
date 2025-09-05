# duf

> Disk Usage/Free Utility. More information: <https://github.com/muesli/duf>.

## Examples

### List accessible devices

```bash
duf
```

### List everything (such as pseudo, duplicate or inaccessible file systems)

```bash
duf --all
```

### Only show specified devices or mount points

```bash
duf path/to/directory1 path/to/directory2 ...
```

### Sort the output by a specified criteria

```bash
duf --sort size|used|avail|usage
```

### Show or hide specific filesystems

```bash
duf --only-fs|hide-fs tmpfs|vfat|ext4|xfs
```

### Sort the output by key

```bash
duf --sort mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem
```

### Change the theme (if `duf` fails to use the right theme)

```bash
duf --theme dark|light
```
