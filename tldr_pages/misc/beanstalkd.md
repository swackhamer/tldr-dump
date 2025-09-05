# beanstalkd

> A simple and generic work-queue server. More information: <https://manned.org/beanstalkd>.

## Examples

### Start the server, listening on port 11300

```bash
beanstalkd
```

### Listen on a specific [p]ort and address

```bash
beanstalkd -l ip_address -p port_number
```

### Persist work queues by saving them to disk

```bash
beanstalkd -b path/to/persistence_directory
```

### Sync to the persistence directory every 500 milliseconds

```bash
beanstalkd -b path/to/persistence_directory -f 500
```
