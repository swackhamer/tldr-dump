# julia

> A high-level, high-performance dynamic programming language for technical computing. More information: <https://docs.julialang.org/en/v1/manual/getting-started/>.

## Examples

### Start a REPL (interactive shell)

```bash
julia
```

### Execute a Julia program and exit

```bash
julia program.jl
```

### Execute a Julia program that takes arguments

```bash
julia program.jl arguments
```

### Evaluate a string containing Julia code

```bash
julia [-e|--eval] 'julia_code'
```

### Evaluate a string of Julia code, passing arguments to it

```bash
julia [-e|--eval] 'for x in ARGS; println(x); end' arguments
```

### Evaluate an expression and print the result

```bash
julia [-E|--print] '(1 - cos(pi/4))/2'
```

### Start Julia in multithreaded mode, using `n` threads

```bash
julia [-t|--threads] n
```
