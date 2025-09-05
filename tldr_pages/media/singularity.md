# singularity

> Manage Singularity containers and images. More information: <https://singularity-docs.readthedocs.io/en/latest/#commands>.

## Examples

### Download a remote image from Sylabs Cloud

```bash
singularity pull --name image.sif library://godlovedc/funny/lolcow:latest
```

### Rebuild a remote image using the latest Singularity image format

```bash
singularity build image.sif docker://godlovedc/lolcow
```

### Start a container from an image and get a shell inside it

```bash
singularity shell image.sif
```

### Start a container from an image and run a command

```bash
singularity exec image.sif command
```

### Start a container from an image and execute the internal runscript

```bash
singularity run image.sif
```

### Build a singularity image from a recipe file

```bash
sudo singularity build image.sif recipe
```
