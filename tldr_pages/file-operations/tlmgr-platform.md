# tlmgr-platform

> Manage TeX Live platforms. More information: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

## Examples

### List all available platforms in the package repository

```bash
tlmgr platform list
```

### Add the executables for a specific platform

```bash
sudo tlmgr platform add platform
```

### Remove the executables for a specific platform

```bash
sudo tlmgr platform remove platform
```

### Auto-detect and switch to the current platform

```bash
sudo tlmgr platform set auto
```

### Switch to a specific platform

```bash
sudo tlmgr platform set platform
```
