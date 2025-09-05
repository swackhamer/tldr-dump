# cargo-publish

> Upload a package to a registry. Note: You have to add an authentication token using `cargo login` before publishing a package. More information: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

## Examples

### Perform checks, create a `.crate` file and upload it to the registry

```bash
cargo publish
```

### Perform checks, create a `.crate` file but don't upload it (equivalent of `cargo package`)

```bash
cargo publish [-n|--dry-run]
```

### Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>)

```bash
cargo publish --registry name
```
