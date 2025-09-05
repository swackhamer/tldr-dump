# cargo-doc

> Build the documentation of Rust packages. More information: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

## Examples

### Build the documentation for the current project and all dependencies

```bash
cargo [d|doc]
```

### Do not build documentation for dependencies

```bash
cargo [d|doc] --no-deps
```

### Build and open the documentation in a browser

```bash
cargo [d|doc] --open
```

### Build and view the documentation of a particular package

```bash
cargo [d|doc] --open [-p|--package] package
```
