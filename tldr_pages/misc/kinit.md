# kinit

> Authenticate a principal with a Kerberos server to gain and cache a ticket. Note: A Kerberos principal can be either a user, service, or application. More information: <https://web.mit.edu/kerberos/krb5-latest/doc/user/user_commands/kinit.html>.

## Examples

### Authenticate a user and obtain a ticket-granting ticket

```bash
kinit username
```

### Renew a ticket-granting ticket

```bash
kinit -R
```

### Specify a lifetime for the ticket

```bash
kinit -l 5h
```

### Specify a total renewable lifetime for the ticket

```bash
kinit -r 1w
```

### Specify a different principal name to authenticate as

```bash
kinit -p principal@REALM
```

### Specify a different keytab file to authenticate with

```bash
kinit -t path/to/keytab
```
