# az-bicep

> Bicep CLI command group. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/bicep>.

## Examples

### Install Bicep CLI

```bash
az bicep install
```

### Build a Bicep file

```bash
az bicep build [-f|--file] path/to/file.bicep
```

### Attempt to decompile an ARM template file to a Bicep file

```bash
az bicep decompile [-f|--file] path/to/template_file.json
```

### Upgrade Bicep CLI to the latest version

```bash
az bicep upgrade
```

### Display the installed version of Bicep CLI

```bash
az bicep version
```

### List all available versions of Bicep CLI

```bash
az bicep list-versions
```

### Uninstall Bicep CLI

```bash
az bicep uninstall
```
