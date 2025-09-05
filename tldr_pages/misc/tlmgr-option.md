# tlmgr-option

> TeX Live settings manager. More information: <https://www.tug.org/texlive/doc/tlmgr.html#option>.

## Examples

### List all TeX Live settings

```bash
tlmgr option showall
```

### List all currently set Tex Live settings

```bash
tlmgr option show
```

### Print all TeX Live settings in JSON format

```bash
tlmgr option showall --json
```

### Show the value of a specific TeX Live setting

```bash
tlmgr option setting
```

### Modify the value of a specific TeX Live setting

```bash
tlmgr option setting value
```

### Set TeX Live to get future updates from the internet after installing from DVD

```bash
tlmgr option repository https://mirror.ctan.org/systems/texlive/tlnet
```
