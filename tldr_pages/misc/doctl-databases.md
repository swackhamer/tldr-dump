# doctl-databases

> Manage your MySQL, Redis, PostgreSQL, and MongoDB database services. More information: <https://docs.digitalocean.com/reference/doctl/reference/databases>.

## Examples

### Run a `doctl databases` command with an access token

```bash
doctl [d|databases] command [-t|--access-token] access_token
```

### Get details for a database cluster

```bash
doctl [d|databases] [g|get]
```

### List your database clusters

```bash
doctl [d|databases] [ls|list]
```

### Create a database cluster

```bash
doctl [d|databases] [c|create] database_name
```

### Delete a cluster

```bash
doctl [d|databases] [rm|delete] database_id
```
