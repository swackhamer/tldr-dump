# tlmgr-pinning

> The pinning action manages the pinning file. More information: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

## Examples

### Show the current pinning data

```bash
tlmgr pinning show
```

### Pin the matching the packages to the given repository

```bash
tlmgr pinning add repository package1 package2 ...
```

### Remove any packages recorded in the pinning file matching the packages for the given repository

```bash
tlmgr pinning remove repository package1 package2 ...
```

### Remove all pinning data for the given repository

```bash
tlmgr pinning remove repository --all
```
