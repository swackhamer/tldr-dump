# influx

> InfluxDB v1 client. More information: <https://docs.influxdata.com/influxdb/v1/tools/influx-cli/use-influx-cli/>.

## Examples

### Connect to an InfluxDB running on localhost with no credentials

```bash
influx
```

### Connect with a specific username (will prompt for a password)

```bash
influx -username username -password ""
```

### Connect to a specific host

```bash
influx -host hostname
```

### Use a specific database

```bash
influx -database database_name
```

### Execute a given command

```bash
influx -execute "influxql_command"
```

### Return output in a specific format

```bash
influx -execute "influxql_command" -format json|csv|column
```
