# dotnet-add-package

> Add or update a .NET package reference in a project file. More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

## Examples

### Add a package to the project in the current directory

```bash
dotnet add package package
```

### Add a package to a specific project

```bash
dotnet add path/to/file.csproj package package
```

### Add a specific version of a package to the project

```bash
dotnet add package package [-v|--version] 1.0.0
```

### Add a package using a specific NuGet source

```bash
dotnet add package package [-s|--source] https://api.nuget.org/v3/index.json
```

### Add a package only when targeting a specific framework

```bash
dotnet add package package [-f|--framework] net7.0
```

### Add and specify the directory where to restore packages (`~/.nuget/packages` by default)

```bash
dotnet add package package --package-directory path/to/directory
```
