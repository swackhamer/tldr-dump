# cradle-deploy

> Manage Cradle deployments. More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

## Examples

### Deploy Cradle to a server

```bash
cradle deploy production
```

### Deploy static assets to Amazon S3

```bash
cradle deploy s3
```

### Deploy static assets including the Yarn "components" directory

```bash
cradle deploy s3 --include-yarn
```

### Deploy static assets including the "upload" directory

```bash
cradle deploy s3 --include-upload
```
