# aws-s3-website

> Set the website configuration for a bucket. See also: `aws s3`. More information: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

## Examples

### Configure a bucket as a static website

```bash
aws s3 website s3://bucket-name --index-document index.html
```

### Configure an error page for the website

```bash
aws s3 website s3://bucket-name --index-document index.html --error-document error.html
```
