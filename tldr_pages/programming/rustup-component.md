# rustup-component

> Modify a toolchain's installed components. Without the `--toolchain` option `rustup` will use the default toolchain. See `rustup help toolchain` for more information about toolchains. More information: <https://rust-lang.github.io/rustup>.

## Examples

### Add a component to a toolchain

```bash
rustup component add --toolchain toolchain component
```

### Remove a component from a toolchain

```bash
rustup component remove --toolchain toolchain component
```

### List installed and available components for a toolchain

```bash
rustup component list --toolchain toolchain
```

### List installed components for a toolchain

```bash
rustup component list --toolchain toolchain --installed
```
