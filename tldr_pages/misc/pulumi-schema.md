# pulumi-schema

> Check a Pulumi package schema for errors. Schema reference: <https://www.pulumi.com/docs/iac/extending-pulumi/schema/>. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_schema/>.

## Examples

### Check a package schema

```bash
pulumi schema check path/to/file
```

### Check a package schema without failing if the reference to a type is missing

```bash
pulumi schema check --allow-dangling-references path/to/file
```

### Display help

```bash
pulumi schema check [-h|--help]
```
