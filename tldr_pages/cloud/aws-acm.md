# aws-acm

> AWS Certificate Manager. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

## Examples

### Import a certificate

```bash
aws acm import-certificate --certificate-arn certificate_arn --certificate certificate --private-key private_key --certificate-chain certificate_chain
```

### List certificates

```bash
aws acm list-certificates
```

### Describe a certificate

```bash
aws acm describe-certificate --certificate-arn certificate_arn
```

### Request a certificate

```bash
aws acm request-certificate --domain-name domain_name --validation-method validation_method
```

### Delete a certificate

```bash
aws acm delete-certificate --certificate-arn certificate_arn
```

### List certificate validations

```bash
aws acm list-certificates --certificate-statuses status
```

### Get certificate details

```bash
aws acm get-certificate --certificate-arn certificate_arn
```

### Update certificate options

```bash
aws acm update-certificate-options --certificate-arn certificate_arn --options options
```
