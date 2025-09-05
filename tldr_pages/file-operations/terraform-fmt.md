# terraform-fmt

> Format configuration according to Terraform language style conventions. More information: <https://developer.hashicorp.com/terraform/cli/commands/fmt>.

## Examples

### Format the configuration in the current directory

```bash
terraform fmt
```

### Format the configuration in the current directory and subdirectories

```bash
terraform fmt -recursive
```

### Display diffs of formatting changes

```bash
terraform fmt -diff
```

### Do not list files that were formatted to `stdout`

```bash
terraform fmt -list=false
```
