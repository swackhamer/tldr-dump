# aws-pricing

> Query services, products, and pricing information from Amazon Web Services. More information: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

## Examples

### List service codes of a specific region

```bash
aws pricing describe-services --region us-east-1
```

### List attributes for a given service code in a specific region

```bash
aws pricing describe-services --service-code AmazonEC2 --region us-east-1
```

### Print pricing information for a service code in a specific region

```bash
aws pricing get-products --service-code AmazonEC2 --region us-east-1
```

### List values for a specific attribute for a service code in a specific region

```bash
aws pricing get-attribute-values --service-code AmazonEC2 --attribute-name instanceType --region us-east-1
```

### Print pricing information for a service code using filters for instance type and location

```bash
aws pricing get-products --service-code AmazonEC2 --filters "Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge" "Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)" --region us-east-1
```
