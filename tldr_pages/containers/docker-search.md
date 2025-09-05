# docker-search

> Search for Docker images on Docker Hub. More information: <https://docs.docker.com/reference/cli/docker/search/>.

## Examples

### Search for Docker images by name or keyword

```bash
docker search keyword
```

### Search for images and only show official ones

```bash
docker search [-f|--filter] is-official=true keyword
```

### Search for images and only show automated builds

```bash
docker search [-f|--filter] is-automated=true keyword
```

### Search for images with a minimum number of stars

```bash
docker search [-f|--filter] stars=number keyword
```

### Limit the number of results

```bash
docker search --limit number keyword
```

### Customize the output format

```bash
docker search [-f|--format] ".Name: .Description" keyword
```
