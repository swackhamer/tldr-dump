# cargo-yank

> Remove a pushed crate from the index. This should only be used when you accidentally release a significantly broken crate. Note: This does not remove any data. The crate is still present after a yank - this just prevents new projects from using it. More information: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

## Examples

### Yank the specified version of a crate

```bash
cargo yank crate@version
```

### Undo a yank (i.e. allow downloading it again)

```bash
cargo yank --undo crate@version
```

### Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>)

```bash
cargo yank --registry name crate@version
```
