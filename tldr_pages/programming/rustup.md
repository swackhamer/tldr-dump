# rustup

> Install, manage, and update Rust toolchains. Some subcommands, such as `toolchain`, `target`, `update`, etc. have their own usage documentation. More information: <https://rust-lang.github.io/rustup>.

## Examples

### Install the nightly toolchain for your system

```bash
rustup install nightly
```

### Switch the default toolchain to nightly so that the `cargo` and `rustc` commands will use it

```bash
rustup default nightly
```

### Use the nightly toolchain when inside the current project but leave global settings unchanged

```bash
rustup override set nightly
```

### Update all toolchains

```bash
rustup update
```

### List installed toolchains

```bash
rustup show
```

### Run `cargo build` with a certain toolchain

```bash
rustup run toolchain cargo build
```

### Open the local Rust documentation in the default web browser

```bash
rustup doc
```
