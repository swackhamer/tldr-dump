# dotnet

> Cross platform .NET tools for .NET Core. Some subcommands such as `build` have their own usage documentation. More information: <https://learn.microsoft.com/dotnet/core/tools>.

## Examples

### Initialize a new .NET project

```bash
dotnet new template_short_name
```

### Restore NuGet packages

```bash
dotnet restore
```

### Build and execute the .NET project in the current directory

```bash
dotnet run
```

### Run a packaged dotnet application (only needs the runtime, the rest of the commands require the .NET Core SDK installed)

```bash
dotnet path/to/application.dll
```
