# tlmgr-remove

> Uninstall TeX Live packages. By default, removed packages will be backed up to `./tlpkg/backups` under the TL installation directory. More information: <https://www.tug.org/texlive/doc/tlmgr.html#remove-option...-pkg>.

## Examples

### Uninstall a TeX Live package

```bash
sudo tlmgr remove package
```

### Simulate uninstalling a package without making any changes

```bash
tlmgr remove --dry-run package
```

### Uninstall a package without its dependencies

```bash
sudo tlmgr remove --no-depends package
```

### Uninstall a package and back it up to a specific directory

```bash
sudo tlmgr remove --backupdir path/to/directory package
```

### Uninstall all of TeX Live, asking for confirmation

```bash
sudo tlmgr remove --all
```
