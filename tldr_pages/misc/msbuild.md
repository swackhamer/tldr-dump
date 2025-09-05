# msbuild

> The Microsoft build tool for Visual Studio project solutions. More information: <https://learn.microsoft.com/visualstudio/msbuild>.

## Examples

### Build the first project file in the current directory

```bash
msbuild
```

### Build a specific project file

```bash
msbuild path/to/project_file
```

### Specify one or more semicolon-separated targets to build

```bash
msbuild path/to/project_file /target:targets
```

### Specify one or more semicolon-separated properties

```bash
msbuild path/to/project_file /property:name=value
```

### Specify the build tools version to use

```bash
msbuild path/to/project_file /toolsversion:version
```

### Display detailed information at the end of the log about how the project was configured

```bash
msbuild path/to/project_file /detailedsummary
```

### Display help

```bash
msbuild /help
```
