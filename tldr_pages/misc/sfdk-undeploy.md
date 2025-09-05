# sfdk-undeploy

> Undeploys build results from a device. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.undeploy.adoc>.

## Examples

### Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`)

```bash
sfdk undeploy --method
```

### Preview undeploy without applying the changes

```bash
sfdk undeploy --method [-n|--dry-run]
```

### Undeploy files in glob pattern `package*`

```bash
sfdk undeploy --method "+package*"
```

### Undeploy all files excluding `ignore*`

```bash
sfdk undeploy --method "-ignore*"
```
