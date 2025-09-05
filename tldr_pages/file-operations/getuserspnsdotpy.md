# getuserspns.py

> Retrieve Service Principal Names (SPNs) associated with Active Directory user accounts. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Enumerate user accounts with an SPN and request their Kerberos TGS tickets

```bash
GetUserSPNs.py domain/username:password -dc-ip domain_controller_ip
```

### Use pass-the-hash authentication

```bash
GetUserSPNs.py domain/username -hashes LM_Hash:NT_Hash -dc-ip domain_controller_ip
```

### Save the output to a file

```bash
GetUserSPNs.py domain/username:password -dc-ip domain_controller_ip -outputfile path/to/output_file
```

### Request only TGS tickets

```bash
GetUserSPNs.py domain/username:password -dc-ip domain_controller_ip -request
```

### Request only TGS tickets using pass-the-hash authentication

```bash
GetUserSPNs.py domain/username -dc-ip domain_controller_ip -hashes LM_Hash:NT_Hash -request
```
