# bear

> A tool to generate compilation databases for `clang` tooling. More information: <https://github.com/rizsotto/Bear>.

## Examples

### Generate `compile_commands.json` by running a build command

```bash
bear -- make
```

### Generate compilation database with a custom output file name

```bash
bear --output path/to/compile_commands.json -- make
```

### Append results to an existing `compile_commands.json` file

```bash
bear --append -- make
```

### Run in verbose mode to get detailed output

```bash
bear --verbose -- make
```

### Force `bear` to use the preload method for command interception

```bash
bear --force-preload -- make
```
