# gcloud-components-install

> Install components of the Google Cloud CLI, along with their dependencies. Installs components at the current version of the Google Cloud CLI without upgrading the existing installation. More information: <https://cloud.google.com/sdk/gcloud/reference/components/install>.

## Examples

### View available components for installation

```bash
gcloud components list
```

### Install one or more components (installs any dependencies as well)

```bash
gcloud components install component_id1 component_id2 ...
```

### Check the current version of Google Cloud CLI

```bash
gcloud version
```

### Update Google Cloud CLI to the latest version

```bash
gcloud components update
```
