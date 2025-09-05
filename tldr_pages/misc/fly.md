# fly

> Tool for concourse-ci. More information: <https://concourse-ci.org/fly.html>.

## Examples

### Authenticate with and save concourse target

```bash
fly [-t|--target] target_name login [-n|--team-name] team_name [-c|--concourse-url] https://ci.example.com
```

### List targets

```bash
fly targets
```

### List pipelines

```bash
fly [-t|--target] target_name pipelines
```

### Upload or update a pipeline

```bash
fly [-t|--target] target_name set-pipeline [-c|--config] pipeline.yml [-p|--pipeline] pipeline_name
```

### Unpause pipeline

```bash
fly [-t|--target] target_name unpause-pipeline [-p|--pipeline] pipeline_name
```

### Show pipeline configuration

```bash
fly [-t|--target] target_name get-pipeline [-p|--pipeline] pipeline_name
```

### Update local copy of fly

```bash
fly [-t|--target] target_name sync
```

### Destroy pipeline

```bash
fly [-t|--target] target_name destroy-pipeline [-p|--pipeline] pipeline_name
```
