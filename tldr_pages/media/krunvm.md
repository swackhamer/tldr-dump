# krunvm

> Create MicroVMs from OCI images. More information: <https://github.com/containers/krunvm>.

## Examples

### Create MicroVM based on Fedora

```bash
krunvm create docker.io/fedora --cpus number_of_vcpus --mem memory_in_megabytes --name "name"
```

### Start a specific image

```bash
krunvm start "image_name"
```

### List images

```bash
krunvm list
```

### Change a specific image

```bash
krunvm changevm --cpus number_of_vcpus --mem memory_in_megabytes --name "new_vm_name" "current_vm_name"
```

### Delete a specific image

```bash
krunvm delete "image_name"
```
