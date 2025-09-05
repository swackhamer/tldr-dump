# sqsc

> An AWS Simple Queue Service client. More information: <https://github.com/yongfei25/sqsc>.

## Examples

### List all queues

```bash
sqsc lq queue_prefix
```

### List all messages in a queue

```bash
sqsc ls queue_name
```

### Copy all messages from one queue to another

```bash
sqsc cp source_queue destination_queue
```

### Move all messages from one queue to another

```bash
sqsc mv source_queue destination_queue
```

### Describe a queue

```bash
sqsc describe queue_name
```

### Query a queue with SQL syntax

```bash
sqsc query "SELECT body FROM queue_name WHERE body LIKE '%user%'"
```

### Pull all messages from a queue into a local SQLite database in your present working directory

```bash
sqsc pull queue_name
```
