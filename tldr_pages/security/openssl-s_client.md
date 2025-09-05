# openssl-s_client

> OpenSSL command to create TLS client connections. More information: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

## Examples

### Display the start and expiry dates for a domain's certificate

```bash
openssl s_client -connect host:port 2>/dev/null | openssl x509 -noout -dates
```

### Display the certificate presented by an SSL/TLS server

```bash
openssl s_client -connect host:port </dev/null
```

### Set the Server Name Indicator (SNI) when connecting to the SSL/TLS server

```bash
openssl s_client -connect host:port -servername hostname
```

### Display the complete certificate chain of an HTTPS server

```bash
openssl s_client -connect host:443 -showcerts </dev/null
```
