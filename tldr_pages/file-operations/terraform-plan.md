# terraform-plan

> Generate and show Terraform execution plans. More information: <https://developer.hashicorp.com/terraform/cli/commands/plan>.

## Examples

### Generate and show the execution plan in the currently directory

```bash
terraform plan
```

### Show a plan to destroy all remote objects that currently exist

```bash
terraform plan -destroy
```

### Show a plan to update the Terraform state and output values

```bash
terraform plan -refresh-only
```

### Specify values for input variables

```bash
terraform plan -var 'name1=value1' -var 'name2=value2'
```

### Focus Terraform's attention on only a subset of resources

```bash
terraform plan -target resource_type.resource_name[instance index]
```

### Output a plan as JSON

```bash
terraform plan -json
```

### Write a plan to a specific file

```bash
terraform plan -no-color > path/to/file
```
