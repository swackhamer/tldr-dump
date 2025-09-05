# openstack-network

> Manage OpenStack network resources. More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/network.html>.

## Examples

### List all networks

```bash
openstack network list
```

### Show details of a network

```bash
openstack network show network_id_or_name
```

### Create a new network with a given name

```bash
openstack network create network_name
```

### Delete a network

```bash
openstack network delete network_id_or_name
```

### Enable a network

```bash
openstack network set --enable network_id_or_name
```

### Disable a network

```bash
openstack network set --disable network_id_or_name
```
