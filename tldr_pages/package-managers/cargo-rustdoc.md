# cargo-rustdoc

> Build the documentation of Rust packages. Similar to `cargo doc`, but you can pass options to `rustdoc`. See `rustdoc --help` for all available options. More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

## Examples

### Pass options to `rustdoc`

```bash
cargo rustdoc -- rustdoc_options
```

### Warn about a documentation lint

```bash
cargo rustdoc -- --warn rustdoc::lint_name
```

### Ignore a documentation lint

```bash
cargo rustdoc -- --allow rustdoc::lint_name
```

### Document the package's library

```bash
cargo rustdoc --lib
```

### Document the specified binary

```bash
cargo rustdoc --bin name
```

### Document the specified example

```bash
cargo rustdoc --example name
```

### Document the specified integration test

```bash
cargo rustdoc --test name
```
