# ghci

> The Glasgow Haskell Compiler's interactive environment. More information: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

## Examples

### Start a REPL (interactive shell)

```bash
ghci
```

### Start a REPL and load the specified Haskell source file

```bash
ghci source_file.hs
```

### Start a REPL and enable a language option

```bash
ghci -Xlanguage_option
```

### Start a REPL and enable some level of compiler warnings (e.g. `all` or `compact`)

```bash
ghci -Wwarning_level
```

### Start a REPL with a colon-separated list of directories for finding source files

```bash
ghci -ipath/to/directory1:path/to/directory2:...
```
