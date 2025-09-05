# aws-s3-ls

> List AWS S3 buckets, folders (prefixes), and files (objects). More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

## Examples

### List all buckets

```bash
aws s3 ls
```

### List files and folders in the root of a bucket (`s3://` is optional)

```bash
aws s3 ls s3://bucket_name
```

### List files and folders directly inside a directory

```bash
aws s3 ls bucket_name/path/to/directory/
```

### List all files in a bucket

```bash
aws s3 ls --recursive bucket_name
```

### List all files in a path with a given prefix

```bash
aws s3 ls --recursive bucket_name/path/to/directory/prefix
```

### Display help

```bash
aws s3 ls help
```
