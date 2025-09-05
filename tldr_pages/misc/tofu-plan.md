# tofu-plan

> Generate and show OpenTofu execution plans. More information: <https://opentofu.org/docs/cli/commands/plan/>.

## Examples

### Generate and show the execution plan in the currently directory

```bash
tofu plan
```

### Show a plan to destroy all remote objects that currently exist

```bash
tofu plan -destroy
```

### Show a plan to update the Tofu state and output values

```bash
tofu plan -refresh-only
```

### Specify values for input variables

```bash
tofu plan -var 'name1=value1' -var 'name2=value2'
```

### Focus Tofu's attention on only a subset of resources

```bash
tofu plan -target resource_type.resource_name[instance index]
```

### Output a plan as JSON

```bash
tofu plan -json
```

### Write a plan to a specific file

```bash
tofu plan -no-color > path/to/file
```
