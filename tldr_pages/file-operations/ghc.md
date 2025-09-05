# ghc

> The Glasgow Haskell Compiler. Compiles and links Haskell source files. More information: <https://downloads.haskell.org/ghc/latest/docs/users_guide/usage.html>.

## Examples

### Find and compile all modules in the current directory

```bash
ghc Main
```

### Compile a single file

```bash
ghc path/to/file.hs
```

### Compile using extra optimization

```bash
ghc -O path/to/file.hs
```

### Stop compilation after generating object files (.o)

```bash
ghc -c path/to/file.hs
```

### Start a REPL (interactive shell)

```bash
ghci
```

### Evaluate a single expression

```bash
ghc -e expression
```
