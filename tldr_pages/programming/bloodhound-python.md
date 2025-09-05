# bloodhound-python

> A Python ingestor for BloodHound, used to enumerate Active Directory relationships. More information: <https://github.com/dirkjanm/BloodHound.py>.

## Examples

### Collect all data using default collection methods (includes groups, sessions, and trusts)

```bash
bloodhound-python --username username --password password --domain domain
```

### Collect data using Kerberos authentication without requiring a plaintext password

```bash
bloodhound-python --collectionmethod All --kerberos --domain domain
```

### Authenticate using NTLM hashes instead of a password

```bash
bloodhound-python --collectionmethod All --username username --hashes LM:NTLM --domain domain
```

### Specify a custom name server for DNS queries

```bash
bloodhound-python --collectionmethod All --username username --password password --domain domain --nameserver nameserver
```

### Save the output files as a compressed ZIP archive

```bash
bloodhound-python --collectionmethod All --username username --password password --domain domain --zip
```
