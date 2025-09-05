# doctl-databases-firewalls

> Manage firewalls for database clusters. More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls>.

## Examples

### Run a `doctl databases firewalls` command with an access token

```bash
doctl [d|databases] [fw|firewalls] command [-t|--access-token] access_token
```

### Retrieve a list of firewall rules for a given database

```bash
doctl [d|databases] [fw|firewalls] [ls|list]
```

### Add a database firewall rule to a given database

```bash
doctl [d|databases] [fw|firewalls] [a|append] database_id --rule droplet|k8s|ip_addr|tag|app:value
```

### Remove a firewall rule for a given database

```bash
doctl [d|databases] [fw|firewalls] [rm|remove] database_id rule_uuid
```
