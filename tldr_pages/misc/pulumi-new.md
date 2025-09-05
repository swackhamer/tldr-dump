# pulumi-new

> Create a new Pulumi project. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_new/>.

## Examples

### Choose a template interactively

```bash
pulumi new
```

### Create a project from a specific template (e.g `azure-python`)

```bash
pulumi new provided-template
```

### Create a project from a local file

```bash
pulumi new path/to/templates/aws-typescript
```

### Create a project from a Git repository

```bash
pulumi new url
```

### Use the specified secrets provider with the <pulumi.com> backend

```bash
pulumi new --secrets-provider passphrase
```
