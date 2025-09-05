# dotnet-tool

> Manage .NET tools and search published tools in NuGet. More information: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

## Examples

### Install a global tool (don't use `--global` for local tools)

```bash
dotnet tool install [-g|--global] dotnetsay
```

### Install tools defined in the local tool manifest

```bash
dotnet tool restore
```

### Update a specific global tool (don't use `--global` for local tools)

```bash
dotnet tool update [-g|--global] tool_name
```

### Uninstall a global tool (don't use `--global` for local tools)

```bash
dotnet tool uninstall [-g|--global] tool_name
```

### List installed global tools (don't use `--global` for local tools)

```bash
dotnet tool list [-g|--global]
```

### Search tools in NuGet

```bash
dotnet tool search search_term
```

### Display help

```bash
dotnet tool [-h|--help]
```
