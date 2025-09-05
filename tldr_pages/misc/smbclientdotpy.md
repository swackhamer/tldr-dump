# smbclient.py

> A Python-based SMB client for interacting with SMB servers. More information: <https://github.com/fortra/impacket>.

## Examples

### Connect to an SMB server with username and password

```bash
smbclient.py domain/username:password@target
```

### Connect using NTLM hashes for authentication

```bash
smbclient.py -hashes LM_HASH:NT_HASH domain/username@target
```

### Connect using Kerberos authentication

```bash
smbclient.py -k domain/username@target
```

### Connect specifying a domain controller IP

```bash
smbclient.py -dc-ip domain_controller_ip domain/username:password@target
```

### Connect to a specific target IP instead of NetBIOS name

```bash
smbclient.py -target-ip target_ip domain/username:password@target
```

### Connect to a non-standard SMB port

```bash
smbclient.py -port port domain/username:password@target
```

### Execute commands from an input file in the SMB shell

```bash
smbclient.py -inputfile path/to/input_file domain/username:password@target
```

### Log SMB client commands to an output file

```bash
smbclient.py -outputfile path/to/output_file domain/username:password@target
```
