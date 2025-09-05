# cargo-report

> Display various kinds of reports. More information: <https://doc.rust-lang.org/cargo/commands/cargo-report.html>.

## Examples

### Display a report of crates which will eventually stop compiling

```bash
cargo report future-incompatibilities
```

### Display a report with the specified Cargo-generated ID

```bash
cargo report future-incompatibilities --id id
```

### Display a report for the specified package

```bash
cargo report future-incompatibilities [-p|--package] package
```
