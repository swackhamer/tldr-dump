# doctl-databases-replica

> Manage read-only replicas associated with a database cluster. More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

## Examples

### Run a `doctl databases replica` command with an access token

```bash
doctl [d|databases] [p|pool] command [-t|--access-token] access_token
```

### Retrieve information about a read-only database replica

```bash
doctl [d|databases] [r|replica] [g|get] database_id replica_name
```

### Retrieve list of read-only database replicas

```bash
doctl [d|databases] [r|replica] [ls|list] database_id
```

### Create a read-only database replica

```bash
doctl [d|databases] [r|replica] [c|create] database_id replica_name
```

### Delete a read-only database replica

```bash
doctl [d|databases] [r|replica] [rm|delete] database_id replica_name
```
