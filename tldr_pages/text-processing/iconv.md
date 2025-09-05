# iconv

> Convert text from one encoding to another. More information: <https://manned.org/iconv>.

## Examples

### Convert file to a specific encoding, and print to `stdout`

```bash
iconv [-f|--from-code] from_encoding [-t|--to-code] to_encoding input_file
```

### Convert file to the current locale's encoding, and output to a file

```bash
iconv [-f|--from-code] from_encoding input_file > output_file
```

### List supported encodings

```bash
iconv [-l|--list]
```
