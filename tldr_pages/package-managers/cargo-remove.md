# cargo-remove

> Remove dependencies from a Rust project's `Cargo.toml` manifest. More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

## Examples

### Remove a dependency from the current project

```bash
cargo remove dependency
```

### Remove a development or build dependency

```bash
cargo remove --dev|build dependency
```

### Remove a dependency of the given target platform

```bash
cargo remove --target target dependency
```
