# tlmgr

> Manage packages and configuration options of an existing TeX Live installation. Some subcommands such as `paper` have their own usage documentation. More information: <https://www.tug.org/texlive/doc/tlmgr.html#ACTIONS>.

## Examples

### Install a package and its dependencies

```bash
tlmgr install package
```

### Remove a package and its dependencies

```bash
tlmgr remove package
```

### Display information about a package

```bash
tlmgr info package
```

### Update all packages

```bash
tlmgr update --all
```

### Show possible updates without updating anything

```bash
tlmgr update --list
```

### Start a GUI version of tlmgr

```bash
tlmgr gui
```

### List all TeX Live configurations

```bash
tlmgr conf
```
