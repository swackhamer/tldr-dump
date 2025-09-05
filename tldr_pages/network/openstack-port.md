# openstack-port

> Manage OpenStack network ports (virtual network interfaces). More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/port.html>.

## Examples

### List all ports

```bash
openstack port list
```

### Show detailed information about a specific port

```bash
openstack port show port_id_or_name
```

### Create a port on a specific network

```bash
openstack port create --network network_id_or_name port_name
```

### Create a port and assign it a fixed IP `192.168.1.50`

```bash
openstack port create --network network_id --fixed-ip subnet=subnet_id,ip-address=192.168.1.50 port_name
```

### Delete a port

```bash
openstack port delete port_id_or_name
```
