# alr

> Ada package manager. Manage Ada toolchains, dependencies, tools and libraries. More information: <https://alire.ada.dev/docs/#first-steps>.

## Examples

### Create a binary or library project

```bash
alr init --bin|--lib project_name
```

### Add a dependency to the project

```bash
alr add crate
```

### Run the compiled binary (no need to do `build` before)

```bash
alr run
```

### Compile the project

```bash
alr build --release|--development|--validation
```
