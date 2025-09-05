# gcloud-config-set

> Set a property in the Google Cloud CLI configuration. Properties control various aspects of Google Cloud CLI behavior. More information: <https://cloud.google.com/sdk/gcloud/reference/config/set>.

## Examples

### Set the project property in the core section

```bash
gcloud config set project project_id
```

### Set the compute zone for future operations

```bash
gcloud config set compute/zone zone_name
```

### Disable prompting to make gcloud suitable for scripting

```bash
gcloud config set disable_prompts true
```

### View the list of properties currently in use

```bash
gcloud config list
```

### Unset a previously set property

```bash
gcloud config unset property_name
```

### Create a new configuration profile

```bash
gcloud config configurations create configuration_name
```

### Switch between different configuration profiles

```bash
gcloud config configurations activate configuration_name
```
