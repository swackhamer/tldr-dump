# cargo-verify-project

> Check the correctness of the `Cargo.toml` manifest and print the result as a JSON object. More information: <https://doc.rust-lang.org/cargo/commands/cargo-verify-project.html>.

## Examples

### Check the correctness of the current project's manifest

```bash
cargo verify-project
```

### Check the correctness of the specified manifest file

```bash
cargo verify-project --manifest-path path/to/Cargo.toml
```
