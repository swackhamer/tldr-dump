# rustup-set

> Alter `rustup` settings. More information: <https://rust-lang.github.io/rustup>.

## Examples

### Set the default host triple

```bash
rustup set default-host host_triple
```

### Set the default profile (`minimal` includes only `rustc`, `rust-std` and `cargo`, whereas `default` adds `rust-docs`, `rustfmt` and `clippy`)

```bash
rustup set profile minimal|default
```

### Set whether `rustup` should update itself when running `rustup update`

```bash
rustup set auto-self-update enable|disable|check-only
```
