# dotnet-build

> Builds a .NET application and its dependencies. More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

## Examples

### Compile the project or solution in the current directory

```bash
dotnet build
```

### Compile a .NET project or solution in debug mode

```bash
dotnet build path/to/project_or_solution
```

### Compile in release mode

```bash
dotnet build [-c|--configuration] Release
```

### Compile without restoring dependencies

```bash
dotnet build --no-restore
```

### Compile with a specific verbosity level

```bash
dotnet build [-v|--verbosity] quiet|minimal|normal|detailed|diagnostic
```

### Compile for a specific runtime

```bash
dotnet build [-r|--runtime] runtime_identifier
```

### Specify the output directory

```bash
dotnet build [-o|--output] path/to/directory
```
