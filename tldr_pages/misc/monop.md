# monop

> Finds and displays signatures of Types and methods inside .NET assemblies. More information: <https://manned.org/monop>.

## Examples

### Show the structure of a Type built-in of the .NET Framework

```bash
monop System.String
```

### List the types in an assembly

```bash
monop -r:path/to/assembly.exe
```

### Show the structure of a Type in a specific assembly

```bash
monop -r:path/to/assembly.dll Namespace.Path.To.Type
```

### Only show members defined in the specified Type

```bash
monop -r:path/to/assembly.dll [-d|--declared-only] Namespace.Path.To.Type
```

### Show private members

```bash
monop -r:path/to/assembly.dll [-p|--private] Namespace.Path.To.Type
```

### Hide obsolete members

```bash
monop -r:path/to/assembly.dll [-f|--filter-obsolete] Namespace.Path.To.Type
```

### List the other assemblies that a specified assembly references

```bash
monop -r:path/to/assembly.dll --refs
```
