# cargo-fetch

> Fetch dependencies of a package from the network. More information: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

## Examples

### Fetch dependencies specified in `Cargo.lock` (for all targets)

```bash
cargo fetch
```

### Fetch dependencies for the specified target

```bash
cargo fetch --target target_triple
```
