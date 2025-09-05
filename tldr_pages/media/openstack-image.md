# openstack-image

> OpenStack Image service, aka OpenStack Glance, allows users to upload and discover data assets meant to be used with other services. More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>.

## Examples

### List available images

```bash
openstack image list --private|--shared|--all
```

### Display image details

```bash
openstack image show --human-readable image_id
```

### Create/upload an image

```bash
openstack image create --file path/to/file --private|--shared|--all image_name
```

### Delete image(s)

```bash
openstack image delete image_id1 image_id2 ...
```

### Save an image locally

```bash
openstack image save --file filename image_id
```
