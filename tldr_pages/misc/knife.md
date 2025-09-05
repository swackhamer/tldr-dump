# knife

> Interact with a Chef server from a local Chef repo. More information: <https://docs.chef.io/knife.html>.

## Examples

### Bootstrap a new node

```bash
knife bootstrap fqdn_or_ip
```

### List all registered nodes

```bash
knife node list
```

### Show a node

```bash
knife node show node_name
```

### Edit a node

```bash
knife node edit node_name
```

### Edit a role

```bash
knife role edit role_name
```

### View a data bag

```bash
knife data bag show data_bag_name data_bag_item
```

### Upload a local cookbook to the Chef server

```bash
knife cookbook upload cookbook_name
```
