# xxd

> Create a hexadecimal representation (hexdump) from a binary file, or vice-versa. See also: `hexyl`, `od`, `hexdump`. More information: <https://manned.org/xxd>.

## Examples

### Generate a hexdump from a binary file and display the output

```bash
xxd input_file
```

### Generate a hexdump from a binary file and save it as a text file

```bash
xxd input_file output_file
```

### Display a more compact output, replacing consecutive zeros (if any) with a star

```bash
xxd [-a|-autoskip] input_file
```

### Display the output with 10 columns of one octet (byte) each

```bash
xxd [-c|-cols] 10 input_file
```

### Display output only up to a length of 32 bytes

```bash
xxd [-l|-len] 32 input_file
```

### Display the output in plain mode, without any gaps between the columns

```bash
xxd [-p|-postscript] input_file
```

### Revert a plaintext hexdump back into binary, and save it as a binary file

```bash
xxd [-r|-revert] [-p|-postscript] input_file output_file
```
