# ipmitool

> Interface with the Intelligent Platform Management Interface (IPMI). More information: <https://manned.org/ipmitool>.

## Examples

### Open IPMI shell on the local hardware

```bash
sudo ipmitool shell
```

### Open IPMI shell on a remote host

```bash
ipmitool -H ip_address -U user_name shell
```
