# seq

> Output a sequence of numbers to `stdout`. More information: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

## Examples

### Sequence from 1 to 10

```bash
seq 10
```

### Every 3rd number from 5 to 20

```bash
seq 5 3 20
```

### Separate the output with a space instead of a newline

```bash
seq [-s|--separator] " " 5 3 20
```

### Format output width to a minimum of 4 digits padding with zeros as necessary

```bash
seq [-f|--format] "%04g" 5 3 20
```
