# linode-cli-volumes

> Manage Linode Volumes. See also: `linode-cli`. More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>.

## Examples

### List current Volumes

```bash
linode-cli volumes list
```

### Create a new Volume and attach it to a specific Linode

```bash
linode-cli volumes create --label volume_label --size size_in_GB --linode-id linode_id
```

### Attach a Volume to a specific Linode

```bash
linode-cli volumes attach volume_id --linode-id linode_id
```

### Detach a Volume from a Linode

```bash
linode-cli volumes detach volume_id
```

### Resize a Volume (Note: Size can only be increased)

```bash
linode-cli volumes resize volume_id --size new_size_in_GB
```

### Delete a Volume

```bash
linode-cli volumes delete volume_id
```
