# raco

> Racket tools. More information: <https://docs.racket-lang.org/raco/>.

## Examples

### Install a package, automatically installing dependencies

```bash
raco pkg install --auto package_source
```

### Install the current directory as a package

```bash
raco pkg install
```

### Build (or rebuild) bytecode, documentation, executables, and metadata indexes for collections

```bash
raco setup collection1 collection2 ...
```

### Run tests in files

```bash
raco test path/to/tests1.rkt path/to/tests2.rkt ...
```

### Search local documentation

```bash
raco docs search_terms
```

### Display help

```bash
raco help
```
