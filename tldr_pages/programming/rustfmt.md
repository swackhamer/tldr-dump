# rustfmt

> Format Rust source code. More information: <https://github.com/rust-lang/rustfmt>.

## Examples

### Format a file, overwriting the original file in-place

```bash
rustfmt path/to/source.rs
```

### Check a file for formatting and display any changes on the console

```bash
rustfmt --check path/to/source.rs
```

### Backup any modified files before formatting (the original file is renamed with a `.bk` extension)

```bash
rustfmt --backup path/to/source.rs
```

### Format code using a specific Rust style edition (formatting rules) verbosely

```bash
rustfmt --style-edition 2015|2018|2021|2024 [-v|--verbose] path/to/source1.rs path/to/source2.rs ...
```

### Format code using a specific Rust edition (language features and parsing)

```bash
rustfmt --edition 2015|2018|2021|2024 path/to/source1.rs path/to/source2.rs ...
```
