# ocamlc

> The OCaml bytecode compiler. Produces executables runnable by the OCaml interpreter. More information: <https://manned.org/ocamlc>.

## Examples

### Create a binary from a source file

```bash
ocamlc path/to/source_file.ml
```

### Create a named binary from a source file

```bash
ocamlc -o path/to/binary path/to/source_file.ml
```

### Automatically generate a module signature (interface) file

```bash
ocamlc -i path/to/source_file.ml
```
