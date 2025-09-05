# cargo-test

> Execute the unit and integration tests of a Rust package. More information: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

## Examples

### Only run tests containing a specific string in their names

```bash
cargo [t|test] test_name
```

### Set the number of simultaneous running test cases

```bash
cargo [t|test] -- --test-threads count
```

### Test artifacts in release mode, with optimizations

```bash
cargo [t|test] [-r|--release]
```

### Test all packages in the workspace

```bash
cargo [t|test] --workspace
```

### Run tests for a specific package

```bash
cargo [t|test] [-p|--package] package
```

### Run tests without hiding output from test executions

```bash
cargo [t|test] -- --nocapture
```
