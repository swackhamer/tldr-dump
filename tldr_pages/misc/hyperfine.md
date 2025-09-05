# hyperfine

> A benchmarking tool. More information: <https://github.com/sharkdp/hyperfine/>.

## Examples

### Run a basic benchmark, performing at least 10 runs

```bash
hyperfine 'make'
```

### Run a comparative benchmark

```bash
hyperfine 'make target1' 'make target2'
```

### Change minimum number of benchmarking runs

```bash
hyperfine [-m|--min-runs] 7 'make'
```

### Perform benchmark with warmup

```bash
hyperfine [-w|--warmup] 5 'make'
```

### Run a command before each benchmark run (to clear caches, etc.)

```bash
hyperfine [-p|--prepare] 'make clean' 'make'
```

### Run a benchmark where a single parameter changes for each run

```bash
hyperfine [-p|--prepare] 'make clean' [-P|--parameter-scan] num_threads 1 10 'make --jobs {num_threads}'
```
