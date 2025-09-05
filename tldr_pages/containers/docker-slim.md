# docker-slim

> Analyze and optimize Docker images. More information: <https://github.com/slimtoolkit/slim>.

## Examples

### Start DockerSlim on interactive mode

```bash
docker-slim
```

### Analyze Docker layers from a specific image

```bash
docker-slim xray --target image:tag
```

### Lint a Dockerfile

```bash
docker-slim lint --target path/to/Dockerfile
```

### Analyze and generate an optimized Docker image

```bash
docker-slim build image:tag
```

### Display help for a subcommand

```bash
docker-slim subcommand --help
```
