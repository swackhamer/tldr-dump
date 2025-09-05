# bacon

> A background code checker for Rust. More information: <https://github.com/Canop/bacon>.

## Examples

### Run `cargo check` whenever a change is detected in the current directory

```bash
bacon
```

### Run `cargo test` whenever a change is detected in the given directory

```bash
bacon test path/to/directory
```

### Run `cargo check` against all targets whenever a change is detected in the current directory

```bash
bacon check-all
```

### Run a specific job whenever a change is detected in the current directory

```bash
bacon run|test|clippy|doc|...
```

### List all currently available jobs

```bash
bacon --list-jobs
```

### Initialize a `bacon.toml` configuration file in the current directory

```bash
bacon --init
```
