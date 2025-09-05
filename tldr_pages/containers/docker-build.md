# docker-build

> Build an image from a Dockerfile. More information: <https://docs.docker.com/reference/cli/docker/buildx/build/>.

## Examples

### Build a Docker image using the Dockerfile in the current directory

```bash
docker build .
```

### Build a Docker image from a Dockerfile at a specified URL

```bash
docker build github.com/creack/docker-firefox
```

### Build a Docker image and tag it

```bash
docker build [-t|--tag] name:tag .
```

### Build a Docker image with no build context

```bash
docker build [-t|--tag] name:tag - < Dockerfile
```

### Do not use the cache when building the image

```bash
docker build --no-cache [-t|--tag] name:tag .
```

### Build a Docker image using a specific Dockerfile

```bash
docker build [-f|--file] Dockerfile .
```

### Build with custom build-time variables

```bash
docker build --build-arg HTTP_PROXY=http://10.20.30.2:1234 --build-arg FTP_PROXY=http://40.50.60.5:4567 .
```
