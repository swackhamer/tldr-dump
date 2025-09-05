# pulumi-state

> Edit the current stack's state. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>.

## Examples

### Delete a resource from the current stack's state

```bash
pulumi state delete
```

### Move a resource from the current stack to another

```bash
pulumi state move resource_urn --dest stack_name
```

### Rename a resource in the current stack's state

```bash
pulumi state rename
```

### Repair an invalid state

```bash
pulumi state repair
```

### Edit a stack's state in the editor specified by the `EDITOR` environment variable

```bash
pulumi state edit --stack stack_name
```

### Display help

```bash
pulumi state [-h|--help]
```
