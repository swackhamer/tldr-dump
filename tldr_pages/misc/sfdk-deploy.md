# sfdk-deploy

> Deploys build results to a device. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.deploy.adoc>.

## Examples

### Deploy using a specified method (`pkcon`, `rsync`, `sdk`, `zypper`, `zypper-dup` or `manual`)

```bash
sfdk deploy --method
```

### Preview deploy without applying the changes

```bash
sfdk deploy --method [-n|--dry-run]
```

### Deploy files in glob pattern `package*`

```bash
sfdk deploy --method "+package*"
```

### Deploy all files excluding `ignore*`

```bash
sfdk deploy --method "-ignore*"
```

### Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`)

```bash
sfdk undeploy --method
```
