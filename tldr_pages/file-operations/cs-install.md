# cs-install

> Install an application in the installation directory onfigured when installing `cs` (to enable the binary to be loaded add to your `.bash_profile` the `$ eval "$(cs install --env)"` command). More information: <https://get-coursier.io/docs/cli-install>.

## Examples

### Install a specific application

```bash
cs install application_name
```

### Install a specific version of an application

```bash
cs install application_name:application_version
```

### Search an application by a specific name

```bash
cs search application_partial_name
```

### Update a specific application if available

```bash
cs update application_name
```

### Update all the installed applications

```bash
cs update
```

### Uninstall a specific application

```bash
cs uninstall application_name
```

### List all installed applications

```bash
cs list
```

### Pass specific Java options to an installed application

```bash
application_name -Jjava_option_name1=value1 -Jjava_option_name2=value2 ...
```
