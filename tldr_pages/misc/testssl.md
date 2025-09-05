# testssl

> Check SSL/TLS protocols and ciphers supported by a server. More information: <https://testssl.sh/doc/testssl.1.html>.

## Examples

### Test a server (run every check) on port 443

```bash
testssl example.com
```

### Test a different port

```bash
testssl example.com:465
```

### Only check available protocols

```bash
testssl --protocols example.com
```

### Only check vulnerabilities

```bash
testssl --vulnerable example.com
```

### Only check HTTP security headers

```bash
testssl --headers example.com
```

### Test other STARTTLS enabled protocols

```bash
testssl --starttls ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql example.com:port
```
