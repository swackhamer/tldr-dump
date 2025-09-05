# cargo-tree

> Display a tree visualization of a dependency graph. Note: In the tree, dependencies of packages marked with `(*)` have already been shown elsewhere in the graph, and so are not repeated. More information: <https://doc.rust-lang.org/cargo/commands/cargo-tree.html>.

## Examples

### Show a dependency tree of the current project

```bash
cargo tree
```

### Only show dependencies up to the specified depth (e.g. when `n` is 1, display only direct dependencies)

```bash
cargo tree --depth n
```

### Do not display the given package (and its dependencies) in the tree

```bash
cargo tree --prune package_spec
```

### Show all occurrences of repeated dependencies

```bash
cargo tree --no-dedupe
```

### Only show normal/build/development dependencies

```bash
cargo tree [-e|--edges] normal|build|dev
```
