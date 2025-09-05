# pulumi-org

> Manage Pulumi Organization configuration. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_org/>.

## Examples

### Display the default organization and current backend

```bash
pulumi org
```

### Display the default organization

```bash
pulumi org get-default
```

### Set the default organization

```bash
pulumi org set-default organization_name
```

### Search for resources in Pulumi Cloud using Pulumi AI with a plaintext natural language query

```bash
pulumi org search ai [-q|--query] "show me all load balancers in my organization"
```

### Display help

```bash
pulumi org [-h|--help]
```
