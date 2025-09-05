# cargo-check

> Check a local package and all of its dependencies for errors. More information: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

## Examples

### Check the current package

```bash
cargo [c|check]
```

### Check all tests

```bash
cargo [c|check] --tests
```

### Check the integration tests in `tests/integration_test1.rs`

```bash
cargo [c|check] --test integration_test1
```

### Check the current package with the features `feature1` and `feature2`

```bash
cargo [c|check] [-F|--features] feature1,feature2
```

### Check the current package with default features disabled

```bash
cargo [c|check] --no-default-features
```
