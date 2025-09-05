# get-nodeversions

> List installed and available Node.js versions for `ps-nvm`. Part of `ps-nvm` and can only be run under PowerShell. More information: <https://github.com/aaronpowell/ps-nvm>.

## Examples

### List all installed Node.js versions

```bash
Get-NodeVersions
```

### List all available Node.js versions

```bash
Get-NodeVersions -Remote
```

### List all available Node.js 20.x versions

```bash
Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"
```
