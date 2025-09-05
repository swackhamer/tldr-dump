# cargo-clean

> Remove generated artifacts in the `target` directory. More information: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

## Examples

### Remove the entire `target` directory

```bash
cargo clean
```

### Remove documentation artifacts (the `target/doc` directory)

```bash
cargo clean --doc
```

### Remove release artifacts (the `target/release` directory)

```bash
cargo clean [-r|--release]
```

### Remove artifacts in the directory of the given profile (in this case, `target/debug`)

```bash
cargo clean --profile dev
```
