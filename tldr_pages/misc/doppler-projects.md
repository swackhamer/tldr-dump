# doppler-projects

> Manage Doppler Projects. More information: <https://docs.doppler.com/docs/cli>.

## Examples

### Get all projects

```bash
doppler projects
```

### Get info for a project

```bash
doppler projects get name|project_id
```

### Create a project

```bash
doppler projects create name
```

### Update a project's name and description

```bash
doppler projects update name|project_id --name "new_name" --description "new_description"
```

### Delete a project

```bash
doppler projects delete name|project_id
```
