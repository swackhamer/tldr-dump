# rabbitmqctl-cluster

> Manage RabbitMQ nodes in a cluster. More information: <https://www.rabbitmq.com/rabbitmqctl.8.html>.

## Examples

### Display the status of the cluster

```bash
rabbitmqctl cluster_status
```

### Display the status of the current node

```bash
rabbitmqctl status
```

### Start the RabbitMQ application on a specific node

```bash
rabbitmqctl [-n|--node] nodename start_app
```

### Stop the RabbitMQ application on a specific node

```bash
rabbitmqctl [-n|--node] nodename stop_app
```

### Stop a specific RabbitMQ node

```bash
rabbitmqctl [-n|--node] nodename stop
```

### Reset a specific RabbitMQ node to a clean state

```bash
rabbitmqctl [-n|--node] nodename reset
```

### Make the current node join an existing cluster

```bash
rabbitmqctl join_cluster nodename
```
