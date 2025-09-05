# pulumi

> Define infrastructure on any cloud using familiar programming languages. Some subcommands such as `up` have their own usage documentation. More information: <https://www.pulumi.com/docs/iac/cli/>.

## Examples

### Create a new project using a template

```bash
pulumi new
```

### Create a new stack using an isolated deployment target

```bash
pulumi stack init
```

### Configure variables (e.g. keys, regions, etc.) interactively

```bash
pulumi config
```

### Preview and deploy changes to a program and/or infrastructure

```bash
pulumi up
```

### Preview deployment changes without performing them (dry-run)

```bash
pulumi preview
```

### Destroy a program and its infrastructure

```bash
pulumi destroy
```

### Use Pulumi locally, independent of a Pulumi Cloud

```bash
pulumi login [-l|--local]
```
