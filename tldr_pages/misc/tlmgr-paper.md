# tlmgr-paper

> Manage paper size options of an TeX Live installation. More information: <https://www.tug.org/texlive/doc/tlmgr.html#paper>.

## Examples

### Show the default paper size used by all TeX Live programs

```bash
tlmgr paper
```

### Set the default paper size for all TeX Live programs to A4

```bash
sudo tlmgr paper a4
```

### Show the default paper size used by a specific TeX Live program

```bash
tlmgr pdftex paper
```

### Set the default paper size for a specific TeX Live program to A4

```bash
sudo tlmgr pdftex paper a4
```

### List all available paper sizes for a specific TeX Live program

```bash
tlmgr pdftex paper --list
```

### Dump the default paper size used by all TeX Live programs in JSON format

```bash
tlmgr paper --json
```
