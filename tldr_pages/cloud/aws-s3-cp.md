# aws-s3-cp

> Copy local files or S3 objects to another location locally or in S3. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

## Examples

### Copy a file from local to a specific bucket

```bash
aws s3 cp path/to/file s3://bucket_name/path/to/remote_file
```

### Copy a specific S3 object into another bucket

```bash
aws s3 cp s3://bucket_name1/path/to/file s3://bucket_name2/path/to/target
```

### Copy a specific S3 object into another bucket keeping the original name

```bash
aws s3 cp s3://bucket_name1/path/to/file s3://bucket_name2
```

### Copy S3 objects to a local directory recursively

```bash
aws s3 cp s3://bucket_name . --recursive
```

### Display help

```bash
aws s3 cp help
```
