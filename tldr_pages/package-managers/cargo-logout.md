# cargo-logout

> Remove an API token from the registry locally. The token is used to authenticate to a package registry. You can add it back using `cargo login`. More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

## Examples

### Remove an API token from the local credential storage (located in `$CARGO_HOME/credentials.toml`)

```bash
cargo logout
```

### Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>)

```bash
cargo logout --registry name
```
