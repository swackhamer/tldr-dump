# chkrootkit

> Scan system for rootkits. More information: <https://manned.org/chkrootkit>.

## Examples

### Enable [q]uiet mode and suppress normal test results

```bash
chkrootkit -q
```

### Enable e[x]pert mode and produce additional outputs

```bash
chkrootkit -x
```

### Enable [d]ebug mode to show all output

```bash
chkrootkit -d
```

### Specify [e]xcluded files for some tests

```bash
chkrootkit -e "path/to/file"
```

### Specify a directory as the [r]oot for testing (e.g. mounted `ext` drives)

```bash
chkrootkit -r path/to/directory
```

### Ignore [n]fs-mounted directories

```bash
chkrootkit -n
```

### Invoke [T]ests and ignore specific filesystem types

```bash
chkrootkit -T filesystemtype
```

### Generate [l]ist of available tests

```bash
chkrootkit -l
```
