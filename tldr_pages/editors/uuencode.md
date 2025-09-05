# uuencode

> Encode binary files into ASCII for transport via mediums that only support simple ASCII encoding. More information: <https://manned.org/uuencode>.

## Examples

### Encode a file and print the result to `stdout`

```bash
uuencode path/to/input_file output_file_name_after_decoding
```

### Encode a file and write the result to a file

```bash
uuencode -o path/to/output_file path/to/input_file output_file_name_after_decoding
```

### Encode a file using Base64 instead of the default uuencode encoding and write the result to a file

```bash
uuencode [-m|--base64] -o path/to/output_file path/to/input_file output_file_name_after_decoding
```
