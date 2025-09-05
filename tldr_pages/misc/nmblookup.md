# nmblookup

> Discover SMB shares. More information: <https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>.

## Examples

### Find hosts in the local network with SMB shares

```bash
nmblookup [-S|--status] '*'
```

### Find hosts in the local network with SMB shares run by SAMBA

```bash
nmblookup [-S|--status] __SAMBA__
```
