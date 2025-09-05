# doctl-databases-maintenance-window

> Schedule, and check the schedule of, maintenance windows for your databases. More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>.

## Examples

### Run a `doctl databases maintenance-window` command with an access token

```bash
doctl [d|databases] [mw|maintenance-window] command [-t|--access-token] access_token
```

### Retrieve details about a database cluster's maintenance windows

```bash
doctl [d|databases] [mw|maintenance-window] [g|get] database_id
```

### Update the maintenance window for a database cluster

```bash
doctl [d|databases] [mw|maintenance-window] [u|update] database_id --day day_of_the_week --hour hour_in_24_hours_format
```
