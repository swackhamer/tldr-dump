# cargo-fmt

> Run `rustfmt` on all source files in a Rust project. More information: <https://github.com/rust-lang/rustfmt>.

## Examples

### Format all source files

```bash
cargo fmt
```

### Check for formatting errors without writing to the files

```bash
cargo fmt --check
```

### Pass arguments to each `rustfmt` call

```bash
cargo fmt -- rustfmt_args
```
