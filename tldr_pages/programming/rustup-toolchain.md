# rustup-toolchain

> Manage Rust toolchains. See `rustup help toolchain` for more information about toolchains. More information: <https://rust-lang.github.io/rustup>.

## Examples

### Install or update a given toolchain

```bash
rustup toolchain install toolchain
```

### Uninstall a toolchain

```bash
rustup toolchain uninstall toolchain
```

### List installed toolchains

```bash
rustup toolchain list
```

### Create a custom toolchain by symlinking to a directory

```bash
rustup toolchain link custom_toolchain_name path/to/directory
```
