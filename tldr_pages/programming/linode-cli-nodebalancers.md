# linode-cli-nodebalancers

> Manage Linode NodeBalancers. See also: `linode-cli`. More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>.

## Examples

### List all NodeBalancers

```bash
linode-cli nodebalancers list
```

### Create a new NodeBalancer

```bash
linode-cli nodebalancers create --region region
```

### View details of a specific NodeBalancer

```bash
linode-cli nodebalancers view nodebalancer_id
```

### Update an existing NodeBalancer

```bash
linode-cli nodebalancers update nodebalancer_id --label new_label
```

### Delete a NodeBalancer

```bash
linode-cli nodebalancers delete nodebalancer_id
```

### List configurations for a NodeBalancer

```bash
linode-cli nodebalancers configs list nodebalancer_id
```

### Add a new configuration to a NodeBalancer

```bash
linode-cli nodebalancers configs create nodebalancer_id --port port --protocol protocol
```
