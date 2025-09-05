# afconvert

> Convert between AFF and raw file formats. More information: <https://manned.org/afconvert.1>.

## Examples

### Use a specific extension (default: `aff`)

```bash
afconvert -a extension path/to/input_file path/to/output_file1 path/to/output_file2 ...
```

### Use a specific compression level (default: `7`)

```bash
afconvert -X0..7 path/to/input_file path/to/output_file1 path/to/output_file2 ...
```
