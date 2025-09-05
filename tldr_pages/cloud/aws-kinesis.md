# aws-kinesis

> Interact with the Amazon Kinesis Data Streams, a service that scales elastically for real-time processing of streaming big data. More information: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

## Examples

### Show all streams in the account

```bash
aws kinesis list-streams
```

### Write one record to a Kinesis stream

```bash
aws kinesis put-record --stream-name name --partition-key key --data base64_encoded_message
```

### Write a record to a Kinesis stream with inline base64 encoding

```bash
aws kinesis put-record --stream-name name --partition-key key --data "$( echo "my raw message" | base64 )"
```

### List the shards available on a stream

```bash
aws kinesis list-shards --stream-name name
```

### Get a shard iterator for reading from the oldest message in a stream's shard

```bash
aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name name --shard-id id
```

### Read records from a shard, using a shard iterator

```bash
aws kinesis get-records --shard-iterator iterator
```
