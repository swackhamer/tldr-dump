# aws-acm-pca

> AWS Certificate Manager Private Certificate Authority. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>.

## Examples

### Create a private certificate authority

```bash
aws acm-pca create-certificate-authority --certificate-authority-configuration ca_config --idempotency-token token --permanent-deletion-time-in-days number
```

### Describe a private certificate authority

```bash
aws acm-pca describe-certificate-authority --certificate-authority-arn ca_arn
```

### List private certificate authorities

```bash
aws acm-pca list-certificate-authorities
```

### Update a certificate authority

```bash
aws acm-pca update-certificate-authority --certificate-authority-arn ca_arn --certificate-authority-configuration ca_config --status status
```

### Delete a private certificate authority

```bash
aws acm-pca delete-certificate-authority --certificate-authority-arn ca_arn
```

### Issue a certificate

```bash
aws acm-pca issue-certificate --certificate-authority-arn ca_arn --certificate-signing-request cert_signing_request --signing-algorithm algorithm --validity validity
```

### Revoke a certificate

```bash
aws acm-pca revoke-certificate --certificate-authority-arn ca_arn --certificate-serial serial --reason reason
```

### Get certificate details

```bash
aws acm-pca get-certificate --certificate-authority-arn ca_arn --certificate-arn cert_arn
```
