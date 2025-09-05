# tofu-fmt

> Format configuration according to OpenTofu language style conventions. More information: <https://opentofu.org/docs/cli/commands/fmt/>.

## Examples

### Format the configuration in the current directory

```bash
tofu fmt
```

### Format the configuration in the current directory and subdirectories

```bash
tofu fmt -recursive
```

### Display diffs of formatting changes

```bash
tofu fmt -diff
```

### Do not list files that were formatted to `stdout`

```bash
tofu fmt -list=false
```
