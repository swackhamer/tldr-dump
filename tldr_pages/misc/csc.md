# csc

> The Microsoft C# Compiler. More information: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

## Examples

### Compile one or more C# files to a CIL executable

```bash
csc path/to/input_file_a.cs path/to/input_file_b.cs
```

### Specify the output filename

```bash
csc /out:path/to/filename path/to/input_file.cs
```

### Compile into a `.dll` library instead of an executable

```bash
csc /target:library path/to/input_file.cs
```

### Reference another assembly

```bash
csc /reference:path/to/library.dll path/to/input_file.cs
```

### Embed a resource

```bash
csc /resource:path/to/resource_file path/to/input_file.cs
```

### Automatically generate XML documentation

```bash
csc /doc:path/to/output.xml path/to/input_file.cs
```

### Specify an icon

```bash
csc /win32icon:path/to/icon.ico path/to/input_file.cs
```

### Strongly-name the resulting assembly with a keyfile

```bash
csc /keyfile:path/to/keyfile path/to/input_file.cs
```
