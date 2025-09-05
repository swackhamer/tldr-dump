# multipass

> Manage Ubuntu virtual machines using native hypervisors. More information: <https://documentation.ubuntu.com/multipass/en/latest/reference/command-line-interface/#>.

## Examples

### List the aliases that can be used to launch an instance

```bash
multipass find
```

### Launch a new instance, set its name and use a cloud-init configuration file

```bash
multipass launch [-n|--name] instance_name --cloud-init configuration_file
```

### List all the created instances and some of their properties

```bash
multipass list
```

### Start a specific instance by name

```bash
multipass start instance_name
```

### Show the properties of an instance

```bash
multipass info instance_name
```

### Open a shell prompt on a specific instance by name

```bash
multipass shell instance_name
```

### Delete an instance by name

```bash
multipass delete instance_name
```

### Mount a directory into a specific instance

```bash
multipass mount path/to/local/directory instance_name:path/to/target/directory
```
