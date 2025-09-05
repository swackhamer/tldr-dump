# cargo

> Manage Rust projects and their module dependencies (crates). Some subcommands such as `build` have their own usage documentation. More information: <https://doc.rust-lang.org/cargo>.

## Examples

### Search for crates

```bash
cargo search search_string
```

### Install a binary crate

```bash
cargo install crate_name
```

### List installed binary crates

```bash
cargo install --list
```

### Create a new binary or library Rust project in the specified directory (or the current working directory by default)

```bash
cargo init --bin|lib path/to/directory
```

### Add a dependency to `Cargo.toml` in the current directory

```bash
cargo add dependency
```

### Build the Rust project in the current directory using the release profile

```bash
cargo [b|build] [-r|--release]
```

### Build the Rust project in the current directory using the nightly compiler (requires `rustup`)

```bash
cargo +nightly [b|build]
```

### Build using a specific number of threads (default is the number of logical CPUs)

```bash
cargo [b|build] --jobs number_of_threads
```
