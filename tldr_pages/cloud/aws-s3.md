# aws-s3

> CLI for AWS S3 - provides storage through web services interfaces. Some subcommands such as `cp` have their own usage documentation. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

## Examples

### Show files in a bucket

```bash
aws s3 ls bucket_name
```

### Sync files and directories from local to bucket

```bash
aws s3 sync path/to/file1 path/to/file2 ... s3://bucket_name
```

### Sync files and directories from bucket to local

```bash
aws s3 sync s3://bucket_name path/to/target
```

### Sync files and directories with exclusions

```bash
aws s3 sync path/to/file1 path/to/file2 ... s3://bucket_name --exclude path/to/file --exclude path/to/directory/*
```

### Remove file from bucket

```bash
aws s3 rm s3://bucket/path/to/file
```

### Preview changes only

```bash
aws s3 any_command --dryrun
```
