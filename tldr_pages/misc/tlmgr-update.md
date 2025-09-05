# tlmgr-update

> Update TeX Live packages. More information: <https://www.tug.org/texlive/doc/tlmgr.html#update-option...-pkg>.

## Examples

### Update all TeX Live packages

```bash
sudo tlmgr update --all
```

### Update tlmgr itself

```bash
sudo tlmgr update --self
```

### Update a specific package

```bash
sudo tlmgr update package
```

### Update all except a specific package

```bash
sudo tlmgr update --all --exclude package
```

### Update all packages, making a backup of the current packages

```bash
sudo tlmgr update --all --backup
```

### Update a specific package without updating its dependencies

```bash
sudo tlmgr update --no-depends package
```

### Simulate updating all packages without making any changes

```bash
sudo tlmgr update --all --dry-run
```
