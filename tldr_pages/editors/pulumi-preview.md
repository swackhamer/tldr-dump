# pulumi-preview

> Show a preview of updates to a stack's resources. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_preview/>.

## Examples

### Show a preview of updates to a stack's resources

```bash
pulumi preview
```

### Show a preview of updates to a stack's resources in JSON format

```bash
pulumi preview [-j|--json]
```

### Preview updates as a rich diff showing overall changes

```bash
pulumi preview --diff
```

### Preview updates using a Policy Pack (without Pulumi Cloud, best on CI/CD)

```bash
pulumi preview --policy-pack path/to/directory
```

### Display help

```bash
pulumi preview [-h|--help]
```
