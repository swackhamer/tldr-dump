# pulumi-stack

> Manage stacks and view stack state. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

## Examples

### Create a new stack

```bash
pulumi stack init stack_name
```

### Show the stack state along with resource URNs

```bash
pulumi stack [-u|--show-urns]
```

### List stacks in the current project

```bash
pulumi stack ls
```

### List stacks across all projects

```bash
pulumi stack ls [-a|--all]
```

### Select an active stack

```bash
pulumi stack select stack_name
```

### Delete a stack

```bash
pulumi stack rm stack_name
```

### Show stack outputs, including secrets, in plaintext

```bash
pulumi stack output --show-secrets
```

### Export the stack state to a JSON file

```bash
pulumi stack export --file path/to/file.json
```
