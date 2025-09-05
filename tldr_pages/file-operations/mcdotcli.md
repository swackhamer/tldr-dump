# mc.cli

> MinIO Client for object storage and filesystems. May be named `mc` or `mcli` on some systems. More information: <https://minio.github.io/mc/>.

## Examples

### Add connection to a S3 server

```bash
mc alias set local http://localhost:9000 access_key secret_key
```

### Create a bucket

```bash
mc mb local/bucket_name
```

### List buckets and their content recursively

```bash
mc ls local --recursive
```
