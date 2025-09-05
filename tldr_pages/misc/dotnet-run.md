# dotnet-run

> Run a .NET application without explicit compile or launch commands. More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>.

## Examples

### Run the project in the current directory

```bash
dotnet run
```

### Run a specific project

```bash
dotnet run --project path/to/file.csproj
```

### Run the project with specific arguments

```bash
dotnet run -- arg1=foo arg2=bar ...
```

### Run the project using a target framework moniker

```bash
dotnet run [-f|--framework] net7.0
```

### Specify architecture and OS, available since .NET 6 (Don't use `--runtime` with these options)

```bash
dotnet run [-a|--arch] x86|x64|arm|arm64 --os win|win7|osx|linux|ios|android
```
