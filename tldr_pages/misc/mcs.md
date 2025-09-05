# mcs

> Mono C# Compiler. More information: <https://manned.org/mcs.1>.

## Examples

### Compile the specified files

```bash
mcs path/to/input_file1.cs path/to/input_file2.cs ...
```

### Specify the output program name

```bash
mcs -out:path/to/file.exe path/to/input_file1.cs path/to/input_file2.cs ...
```

### Specify the output program type

```bash
mcs -target:exe|winexe|library|module path/to/input_file1.cs path/to/input_file2.cs ...
```
