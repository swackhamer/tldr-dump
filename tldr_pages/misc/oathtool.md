# oathtool

> OATH one-time password tool. More information: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

## Examples

### Generate TOTP token (behaves like Google Authenticator)

```bash
oathtool --totp [-b|--base32] "secret"
```

### Generate a TOTP token for a specific time

```bash
oathtool --totp [-N|--now] "2004-02-29 16:21:42" [-b|--base32] "secret"
```

### Validate a TOTP token

```bash
oathtool --totp [-b|--base32] "secret" "token"
```
