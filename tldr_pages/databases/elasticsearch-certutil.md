# elasticsearch-certutil

> Generate and manage SSL certificates for Elasticsearch security. More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/certutil.html>.

## Examples

### Generate a new Certificate Authority (CA) with default options

```bash
elasticsearch-certutil ca
```

### Generate a new certificate using the built-in CA

```bash
elasticsearch-certutil cert
```

### Generate certificates non-interactively and output PEM files

```bash
elasticsearch-certutil cert [-s|--silent] --pem
```

### Generate HTTP certificates with the built-in CA

```bash
elasticsearch-certutil http
```

### Generate transport certificates non-interactively

```bash
elasticsearch-certutil transport [-s|--silent]
```

### Generate a certificate signing request (CSR)

```bash
elasticsearch-certutil csr
```

### Generate encrypted keystore passwords

```bash
elasticsearch-certutil password
```

### Generate a keystore password with a specified value

```bash
elasticsearch-certutil password --pass password
```
