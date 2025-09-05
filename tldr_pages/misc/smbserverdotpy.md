# smbserver.py

> A Python-based SMB server for hosting shares (requires root for port 445). More information: <https://github.com/fortra/impacket>.

## Examples

### Set up a basic SMB share

```bash
smbserver.py sharename path/to/share
```

### Set up a share with a custom comment

```bash
smbserver.py -comment my_share sharename path/to/share
```

### Set up a share with username and password authentication

```bash
smbserver.py -username username -password password sharename path/to/share
```

### Set up a share with NTLM hash authentication

```bash
smbserver.py -hashes LMHASH:NTHASH sharename path/to/share
```

### Set up a share on a specific interface

```bash
smbserver.py [-ip|--interface-address] interface_ip_address sharename path/to/share
```

### Set up a share on a non-standard SMB port

```bash
smbserver.py -port port sharename path/to/share
```

### Set up a share with SMB2 support

```bash
smbserver.py -smb2support sharename path/to/share
```

### Set up a share and log commands to an output file

```bash
smbserver.py -outputfile path/to/output_file sharename path/to/share
```
