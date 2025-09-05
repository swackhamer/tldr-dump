# cargo-clippy

> A collection of lints to catch common mistakes and improve your Rust code. More information: <https://github.com/rust-lang/rust-clippy>.

## Examples

### Run checks over the code in the current directory

```bash
cargo clippy
```

### Require that `Cargo.lock` is up to date

```bash
cargo clippy --locked
```

### Run checks on all packages in the workspace

```bash
cargo clippy --workspace
```

### Run checks for a package

```bash
cargo clippy --package package
```

### Run checks for a lint group (see <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>)

```bash
cargo clippy -- [-W|--warn] clippy::lint_group
```

### Treat warnings as errors

```bash
cargo clippy -- [-D|--deny] warnings
```

### Run checks and ignore warnings

```bash
cargo clippy -- [-A|--allow] warnings
```

### Apply Clippy suggestions automatically

```bash
cargo clippy --fix
```
