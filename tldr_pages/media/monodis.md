# monodis

> The Mono Common Intermediate Language (CIL) disassembler. More information: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>.

## Examples

### Disassemble an assembly to textual CIL

```bash
monodis path/to/assembly.exe
```

### Save the output to a file

```bash
monodis --output=path/to/output.il path/to/assembly.exe
```

### Show information about an assembly

```bash
monodis --assembly path/to/assembly.dll
```

### List the references of an assembly

```bash
monodis --assemblyref path/to/assembly.exe
```

### List all the methods in an assembly

```bash
monodis --method path/to/assembly.exe
```

### List resources embedded within an assembly

```bash
monodis --manifest path/to/assembly.dll
```

### Extract all the embedded resources to the current directory

```bash
monodis --mresources path/to/assembly.dll
```
