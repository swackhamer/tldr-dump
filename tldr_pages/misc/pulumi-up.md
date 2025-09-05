# pulumi-up

> Create or update the resources in a stack. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

## Examples

### Preview and deploy changes to a program and/or infrastructure

```bash
pulumi up
```

### Automatically approve and perform the update after previewing it

```bash
pulumi up [-y|--yes]
```

### Preview and deploy changes in a specific stack

```bash
pulumi up [-s|--stack] stack
```

### Don't display stack outputs

```bash
pulumi up --suppress-outputs
```

### Continue updating the resources, even if an error is encountered

```bash
pulumi up --continue-on-error
```
