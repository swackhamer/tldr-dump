# makensis

> Cross-platform compiler for NSIS installers. It compiles a NSIS script into a Windows installer executable. More information: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

## Examples

### Compile a NSIS script

```bash
makensis path/to/file.nsi
```

### Compile a NSIS script in strict mode (treat warnings as errors)

```bash
makensis -WX path/to/file.nsi
```

### Display help for a specific command

```bash
makensis -CMDHELP command
```
