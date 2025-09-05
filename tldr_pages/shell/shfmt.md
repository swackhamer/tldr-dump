# shfmt

> Shell parser, formatter and interpreter. More information: <https://pkg.go.dev/mvdan.cc/sh>.

## Examples

### Print a formatted version of a shell script

```bash
shfmt path/to/file
```

### List unformatted files

```bash
shfmt --list path/to/directory
```

### Write the result to the file instead of printing it to the terminal

```bash
shfmt --write path/to/file
```

### Simplify the code, removing redundant pieces of syntax (i.e. removing "$" from vars in expressions)

```bash
shfmt --simplify path/to/file
```
