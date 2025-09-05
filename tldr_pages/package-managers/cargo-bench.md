# cargo-bench

> Compile and execute benchmarks. More information: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

## Examples

### Execute all benchmarks of a package

```bash
cargo bench
```

### Don't stop when a benchmark fails

```bash
cargo bench --no-fail-fast
```

### Compile, but don't run benchmarks

```bash
cargo bench --no-run
```

### Benchmark the specified benchmark

```bash
cargo bench --bench benchmark
```

### Benchmark with the given profile (default: `bench`)

```bash
cargo bench --profile profile
```

### Benchmark all example targets

```bash
cargo bench --examples
```

### Benchmark all binary targets

```bash
cargo bench --bins
```

### Benchmark the package's library

```bash
cargo bench --lib
```
