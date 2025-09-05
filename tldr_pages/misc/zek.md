# zek

> Generate a Go struct from XML. More information: <https://github.com/miku/zek>.

## Examples

### Generate a Go struct from a given XML from `stdin` and display output on `stdout`

```bash
cat path/to/input.xml | zek
```

### Generate a Go struct from a given XML from `stdin` and send output to a file

```bash
curl -s https://url/to/xml | zek -o path/to/output.go
```

### Generate an example Go program from a given XML from `stdin` and send output to a file

```bash
cat path/to/input.xml | zek -p -o path/to/output.go
```
