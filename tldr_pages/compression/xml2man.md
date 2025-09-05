# xml2man

> Compile MPGL to mdoc. More information: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

## Examples

### Compile an MPGL file to a viewable man page

```bash
xml2man path/to/command_file.mxml
```

### Compile an MPGL file to a specific output file

```bash
xml2man path/to/service_file.mxml path/to/service_file.7
```

### Compile an MPGL file to a specific output file, overwriting if it already exists

```bash
xml2man -f path/to/function_file.mxml path/to/function_file.3
```
