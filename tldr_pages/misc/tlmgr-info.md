# tlmgr-info

> Show information about TeX Live packages. More information: <https://www.tug.org/texlive/doc/tlmgr.html#info>.

## Examples

### List all available TeX Live packages, prefexing installed ones with `i`

```bash
tlmgr info
```

### List all available collections

```bash
tlmgr info collections
```

### List all available schemes

```bash
tlmgr info scheme
```

### Show information about a specific package

```bash
tlmgr info package
```

### List all files contained in a specific package

```bash
tlmgr info package --list
```

### List all installed packages

```bash
tlmgr info --only-installed
```

### Show only specific information about a package

```bash
tlmgr info package --data "name,category,installed,size,depends,..."
```

### Print all available packages as JSON encoded array

```bash
tlmgr info --json
```
