# skopeo

> Container image management toolbox. Provides various utility commands to manage remote container images. More information: <https://github.com/containers/skopeo>.

## Examples

### Inspect a remote image from a registry

```bash
skopeo inspect docker://registry_hostname/image:tag
```

### List available tags for a remote image

```bash
skopeo list-tags docker://registry_hostname/image
```

### Download an image from a registry

```bash
skopeo copy docker://registry_hostname/image:tag dir:path/to/directory
```

### Copy an image from one registry to another

```bash
skopeo copy docker://source_registry/image:tag docker://destination_registry/image:tag
```

### Delete an image from a registry

```bash
skopeo delete docker://registry_hostname/image:tag
```

### Log in to a registry

```bash
skopeo login --username username registry_hostname
```
