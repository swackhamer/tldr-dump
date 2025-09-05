# step

> An easy-to-use CLI tool for building, operating, and automating Public Key Infrastructure (PKI) systems and workflows. See also: `openssl`. More information: <https://smallstep.com/docs/step-cli/>.

## Examples

### Inspect the contents of a certificate

```bash
step certificate inspect path/to/certificate.crt
```

### Create a root CA certificate and a key (append `--no-password --insecure` to skip private key password protection)

```bash
step certificate create "Example Root CA" path/to/root-ca.crt path/to/root-ca.key --profile root-ca
```

### Generate a certificate for a specific hostname and sign it with the root CA (generating a CSR can be skipped for simplification)

```bash
step certificate create hostname.example.com path/to/hostname.crt path/to/hostname.key --profile leaf --ca path/to/root-ca.crt --ca-key path/to/root-ca.key
```

### Verify a certificate chain

```bash
step certificate verify path/to/hostname.crt --roots path/to/root-ca.crt --verbose
```

### Convert a PEM format certificate to DER and write it to disk

```bash
step certificate format path/to/certificate.pem --out path/to/certificate.der
```

### Install or uninstall a root certificate in the system's default trust store

```bash
step certificate install|uninstall path/to/root-ca.crt
```

### Create a RSA/EC private and public keypair (append `--no-password --insecure` to skip private key password protection)

```bash
step crypto keypair path/to/public_key path/to/private_key --kty RSA|EC
```

### Display help for subcommands

```bash
step path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh --help
```
