# json5

> Convert JSON5 files to JSON. More information: <https://json5.org>.

## Examples

### Convert JSON5 `stdin` to JSON `stdout`

```bash
echo input | json5
```

### Convert a JSON5 file to JSON and output to `stdout`

```bash
json5 path/to/input_file.json5
```

### Convert a JSON5 file to the specified JSON file

```bash
json5 path/to/input_file.json5 --out-file path/to/output_file.json
```

### Validate a JSON5 file

```bash
json5 path/to/input_file.json5 --validate
```

### Specify the number of spaces to indent by (or "t" for tabs)

```bash
json5 --space indent_amount
```

### Display help

```bash
json5 --help
```
