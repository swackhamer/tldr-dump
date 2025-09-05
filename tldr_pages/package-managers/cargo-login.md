# cargo-login

> Save an API token from the registry locally. The token is used to authenticate to a package registry. You can remove it using `cargo logout`. More information: <https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

## Examples

### Add an API token to the local credential storage (located in `$CARGO_HOME/credentials.toml`)

```bash
cargo login
```

### Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>)

```bash
cargo login --registry name
```
