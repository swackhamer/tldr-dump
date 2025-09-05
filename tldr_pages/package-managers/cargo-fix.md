# cargo-fix

> Automatically fix lint warnings reported by `rustc`. More information: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

## Examples

### Fix code even if it already has compiler errors

```bash
cargo fix --broken-code
```

### Fix code even if the working directory has changes

```bash
cargo fix --allow-dirty
```

### Migrate a package to the next Rust edition

```bash
cargo fix --edition
```

### Fix the package's library

```bash
cargo fix --lib
```

### Fix the specified integration test

```bash
cargo fix --test name
```

### Fix all members in the workspace

```bash
cargo fix --workspace
```
