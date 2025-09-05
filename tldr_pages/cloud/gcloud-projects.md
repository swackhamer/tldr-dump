# gcloud-projects

> Manage project access policies in Google Cloud. See also: `gcloud`. More information: <https://cloud.google.com/sdk/gcloud/reference/projects>.

## Examples

### Create a new project

```bash
gcloud projects create project_id|project_number
```

### List all active projects

```bash
gcloud projects list
```

### Display metadata for a project

```bash
gcloud projects describe project_id
```

### Delete a project

```bash
gcloud projects delete project_id|project_number
```

### Add an IAM policy binding to a specified project

```bash
gcloud projects add-iam-policy-binding project_id --member principal --role role
```
