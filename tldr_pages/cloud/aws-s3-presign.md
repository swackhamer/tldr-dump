# aws-s3-presign

> Generate pre-signed URLs for Amazon S3 objects. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

## Examples

### Generate a pre-signed URL for a specific S3 object that is valid for one hour

```bash
aws s3 presign s3://bucket_name/path/to/file
```

### Generate a pre-signed URL valid for a specific lifetime

```bash
aws s3 presign s3://bucket_name/path/to/file --expires-in duration_in_seconds
```

### Display help

```bash
aws s3 presign help
```
