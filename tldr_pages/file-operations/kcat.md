# kcat

> Apache Kafka producer and consumer tool. More information: <https://github.com/edenhill/kcat>.

## Examples

### Consume messages starting with the newest offset

```bash
kcat -C -t topic -b brokers
```

### Consume messages starting with the oldest offset and exit after the last message is received

```bash
kcat -C -t topic -b brokers -o beginning -e
```

### Consume messages as a Kafka consumer group

```bash
kcat -G group_id topic -b brokers
```

### Publish message by reading from `stdin`

```bash
echo message | kcat -P -t topic -b brokers
```

### Publish messages by reading from a file

```bash
kcat -P -t topic -b brokers path/to/file
```

### List metadata for all topics and brokers

```bash
kcat -L -b brokers
```

### List metadata for a specific topic

```bash
kcat -L -t topic -b brokers
```

### Get offset for a topic/partition for a specific point in time

```bash
kcat -Q -t topic:partition:unix_timestamp -b brokers
```
