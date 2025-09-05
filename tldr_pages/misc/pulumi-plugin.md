# pulumi-plugin

> Manage language and resource provider plugins manually. Other commands manage these automatically. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_plugin/>.

## Examples

### List all plugins on the downloaded cache

```bash
pulumi plugin ls
```

### List plugins being used by the current project in JSON format

```bash
pulumi plugin [-p|--project] [-j|--json]
```

### Install a plugin kind (e.g resource) with the latest version or a specific one

```bash
pulumi plugin install kind name version
```

### Remove a plugin kind (e.g. resource) and interactively pick a version or provide a specific one

```bash
pulumi plugin rm kind name version
```

### Display help

```bash
pulumi plugin [-h|--help]
```
