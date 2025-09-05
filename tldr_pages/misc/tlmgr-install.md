# tlmgr-install

> Install TeX Live packages. More information: <https://www.tug.org/texlive/doc/tlmgr.html#install-option...-pkg>.

## Examples

### Install a package and its dependencies

```bash
sudo tlmgr install package
```

### Reinstall a package

```bash
sudo tlmgr install --reinstall package
```

### Simulate installing a package without making any changes

```bash
tlmgr install --dry-run package
```

### Install a package without its dependencies

```bash
sudo tlmgr install --no-depends package
```

### Install a package from a specific file

```bash
sudo tlmgr install --file path/to/package
```
