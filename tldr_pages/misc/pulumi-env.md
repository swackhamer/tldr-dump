# pulumi-env

> Manage Pulumi environments. More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

## Examples

### List all environments

```bash
pulumi env ls
```

### Create an environment

```bash
pulumi env init environment_name
```

### Set a value in an environment

```bash
pulumi env set environment_name key value
```

### Edit an environment definition

```bash
pulumi env edit environment_name
```

### Delete a value from an environment

```bash
pulumi env rm environment_name key
```

### Delete an environment entirely

```bash
pulumi env rm environment_name
```

### Display help

```bash
pulumi env [-h|--help]
```
