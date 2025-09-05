# shc

> Generic shell script compiler. More information: <https://manned.org/shc>.

## Examples

### Compile a shell script

```bash
shc -f script
```

### Compile a shell script and specify an output binary file

```bash
shc -f script -o binary
```

### Compile a shell script and set an expiration date for the executable

```bash
shc -f script -e dd/mm/yyyy
```

### Compile a shell script and set a message to display upon expiration

```bash
shc -f script -e dd/mm/yyyy -m "Please contact your provider"
```
