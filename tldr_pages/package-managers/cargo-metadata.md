# cargo-metadata

> Output the workspace members and resolved dependencies of current package as JSON. Note: The output format is subject to change in future versions of Cargo. More information: <https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

## Examples

### Print the workspace members and resolved dependencies of the current package

```bash
cargo metadata
```

### Print only the workspace members and do not fetch dependencies

```bash
cargo metadata --no-deps
```

### Print metadata in a specific format based on the specified version

```bash
cargo metadata --format-version version
```

### Print metadata with the `resolve` field including dependencies only for the given target triple (Note: The `packages` array will still include the dependencies for all targets)

```bash
cargo metadata --filter-platform target_triple
```
