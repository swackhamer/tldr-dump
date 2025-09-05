# cargo-rustc

> Compile a Rust package. Similar to `cargo build`, but you can pass extra options to the compiler. See `rustc --help` for all available options. More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

## Examples

### Build the package and pass options to `rustc`

```bash
cargo rustc -- rustc_options
```

### Build artifacts in release mode, with optimizations

```bash
cargo rustc [-r|--release]
```

### Compile with architecture-specific optimizations for the current CPU

```bash
cargo rustc [-r|--release] -- -C target-cpu=native
```

### Compile with speed optimizations

```bash
cargo rustc -- -C opt-level 1|2|3
```

### Compile with [s]ize optimizations (`z` also turns off loop vectorization)

```bash
cargo rustc -- -C opt-level s|z
```

### Check if your package uses unsafe code

```bash
cargo rustc --lib -- -D unsafe-code
```

### Build a specific package

```bash
cargo rustc [-p|--package] package
```

### Build only the specified binary

```bash
cargo rustc --bin name
```
