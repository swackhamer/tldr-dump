# cargo-run

> Run the current Cargo package. Note: The working directory of the executed binary will be set to the current working directory. More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

## Examples

### Run the default binary target

```bash
cargo [r|run]
```

### Run the specified binary

```bash
cargo [r|run] --bin name
```

### Run the specified example

```bash
cargo [r|run] --example name
```

### Activate a space or comma separated list of features

```bash
cargo [r|run] [-F|--features] "feature1 feature2 ..."
```

### Disable the default features

```bash
cargo [r|run] --no-default-features
```

### Activate all available features

```bash
cargo [r|run] --all-features
```

### Run with the given profile

```bash
cargo [r|run] --profile name
```
