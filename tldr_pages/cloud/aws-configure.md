# aws-configure

> Manage configuration for the AWS CLI. More information: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

## Examples

### Configure AWS CLI interactively (creates a new configuration or updates the default)

```bash
aws configure
```

### Configure a named profile for AWS CLI interactively (creates a new profile or updates an existing one)

```bash
aws configure --profile profile_name
```

### Display the value from a specific configuration variable

```bash
aws configure get name
```

### Display the value for a configuration variable in a specific profile

```bash
aws configure get name --profile profile_name
```

### Set the value of a specific configuration variable

```bash
aws configure set name value
```

### Set the value of a configuration variable in a specific profile

```bash
aws configure set name value --profile profile_name
```

### List the configuration entries

```bash
aws configure list
```

### List the configuration entries for a specific profile

```bash
aws configure list --profile profile_name
```
