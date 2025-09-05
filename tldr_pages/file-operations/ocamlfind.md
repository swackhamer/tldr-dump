# ocamlfind

> The findlib package manager for OCaml. Simplifies linking executables with external libraries. More information: <https://manned.org/ocamlfind>.

## Examples

### Compile a source file to a native binary and link with packages

```bash
ocamlfind ocamlopt -package package1,package2,... -linkpkg -o path/to/executable path/to/source.ml
```

### Compile a source file to a bytecode binary and link with packages

```bash
ocamlfind ocamlc -package package1,package2,... -linkpkg -o path/to/executable path/to/source.ml
```

### Cross-compile for a different platform

```bash
ocamlfind -toolchain cross-toolchain ocamlopt -o path/to/executable path/to/source.ml
```
