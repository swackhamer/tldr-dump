# pulumi-refresh

> Refresh the resources in a stack. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_refresh/>.

## Examples

### Compare the current stack's state with the state in the cloud provider and adopt any changes into the current stack

```bash
pulumi refresh
```

### Refresh resources in the current stack and show the operation as a rich diff

```bash
pulumi refresh --diff
```

### Refresh resources in the current stack and return an error if any changes occur during the refresh

```bash
pulumi refresh --expect-no-changes
```

### Only show a preview of the refresh, but don't perform the refresh itself

```bash
pulumi refresh --preview-only
```

### The name of the stack to operate on (defaults to the current stack)

```bash
pulumi refresh [-s|--stack] stack_name
```

### Display help

```bash
pulumi refresh [-h|--help]
```
