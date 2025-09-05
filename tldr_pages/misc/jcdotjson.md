# jc.json

> Convert the output of multiple commands to JSON. More information: <https://github.com/kellyjonbrazil/jc>.

## Examples

### Convert command output to JSON via pipe

```bash
ifconfig | jc --ifconfig
```

### Convert command output to JSON via magic syntax

```bash
jc ifconfig
```

### Output pretty JSON via pipe

```bash
ifconfig | jc --ifconfig [-p|--pretty]
```

### Output pretty JSON via magic syntax

```bash
jc [-p|--pretty] ifconfig
```
