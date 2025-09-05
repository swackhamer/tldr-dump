# olevba

> Parse OLE and OpenXML files (e.g., DOC, XLS, PPT, etc.) to extract VBA macros, deobfuscate, and analyze malicious code. Part of the `python-oletools` suite. More information: <https://github.com/decalage2/oletools>.

## Examples

### Analyze a file, showing both macro code and analysis results

```bash
olevba path/to/file
```

### Recursively analyze all supported files in a directory

```bash
olevba -r path/to/directory
```

### Provide a password for encrypted Microsoft Office files (may be repeated)

```bash
olevba [-p|--password] password path/to/encrypted_file
```

### Display only analysis results, without showing macro source code

```bash
olevba [-a|--analysis] path/to/file
```

### Display only macro source code

```bash
olevba [-c|--code] path/to/file
```

### Show obfuscated strings and their decoded content

```bash
olevba --decode path/to/file
```
