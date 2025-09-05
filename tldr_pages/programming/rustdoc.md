# rustdoc

> Generate documentation for a Rust crate. More information: <https://doc.rust-lang.org/stable/rustdoc>.

## Examples

### Generate documentation from the crate's root

```bash
rustdoc src/lib.rs
```

### Pass a name for the project

```bash
rustdoc src/lib.rs --crate-name name
```

### Generate documentation from Markdown files

```bash
rustdoc path/to/file.md
```

### Specify the output directory

```bash
rustdoc src/lib.rs --out-dir path/to/output_directory
```
