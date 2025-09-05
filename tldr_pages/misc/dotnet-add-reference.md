# dotnet-add-reference

> Add .NET project-to-project references. More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

## Examples

### Add a reference to the project in the current directory

```bash
dotnet add reference path/to/reference.csproj
```

### Add multiple references to the project in the current directory

```bash
dotnet add reference path/to/reference1.csproj path/to/reference2.csproj ...
```

### Add a reference to the specific project

```bash
dotnet add path/to/project.csproj reference path/to/reference.csproj
```

### Add multiple references to the specific project

```bash
dotnet add path/to/project.csproj reference path/to/reference1.csproj path/to/reference2.csproj ...
```
