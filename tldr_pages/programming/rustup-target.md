# rustup-target

> Modify a toolchain's supported targets. Without the `--toolchain` option `rustup` will use the default toolchain. See `rustup help toolchain` for more information about toolchains. More information: <https://rust-lang.github.io/rustup>.

## Examples

### Add a target to a toolchain

```bash
rustup target add --toolchain toolchain target
```

### Remove a target from a toolchain

```bash
rustup target remove --toolchain toolchain target
```

### List available and installed targets for a toolchain

```bash
rustup target list --toolchain toolchain
```

### List installed targets for a toolchain

```bash
rustup target list --toolchain toolchain --installed
```
