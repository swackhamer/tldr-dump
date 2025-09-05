# cargo-build

> Compile a local package and all of its dependencies. More information: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

## Examples

### Build the package or packages defined by the `Cargo.toml` manifest file in the local path

```bash
cargo [b|build]
```

### Build artifacts in release mode, with optimizations

```bash
cargo [b|build] [-r|--release]
```

### Require that `Cargo.lock` is up to date

```bash
cargo [b|build] --locked
```

### Build all packages in the workspace

```bash
cargo [b|build] --workspace
```

### Build a specific package

```bash
cargo [b|build] [-p|--package] package
```

### Build only the specified binary

```bash
cargo [b|build] --bin name
```

### Build only the specified test target

```bash
cargo [b|build] --test test_name
```
