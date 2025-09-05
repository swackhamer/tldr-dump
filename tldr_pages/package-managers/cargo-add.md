# cargo-add

> Add dependencies to a Rust project's `Cargo.toml` manifest. More information: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

## Examples

### Add the latest version of a dependency to the current project

```bash
cargo add dependency
```

### Add a specific version of a dependency

```bash
cargo add dependency@version
```

### Add a dependency and enable one or more specific features

```bash
cargo add dependency [-F|--features] feature_1,feature_2
```

### Add an optional dependency, which then gets exposed as a feature of the crate

```bash
cargo add dependency --optional
```

### Add a local crate as a dependency

```bash
cargo add --path path/to/crate_directory
```

### Add a development or build dependency

```bash
cargo add dependency --dev|build
```

### Add a dependency with all default features disabled

```bash
cargo add dependency --no-default-features
```
