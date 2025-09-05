# mkcert

> Make locally-trusted development certificates. More information: <https://github.com/FiloSottile/mkcert>.

## Examples

### Install the local CA in the system trust store

```bash
mkcert -install
```

### Generate certificate and private key for a given domain

```bash
mkcert example.org
```

### Generate certificate and private key for multiple domains

```bash
mkcert example.org myapp.dev 127.0.0.1
```

### Generate wildcard certificate and private key for a given domain and its subdomains

```bash
mkcert "*.example.it"
```

### Uninstall the local CA

```bash
mkcert -uninstall
```
