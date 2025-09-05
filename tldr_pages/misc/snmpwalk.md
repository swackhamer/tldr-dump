# snmpwalk

> SNMP query tool. More information: <https://manned.org/snmpwalk>.

## Examples

### Query the system information of a remote host using SNMPv1 and a community string

```bash
snmpwalk -v 1 -c community ip
```

### Query system information on a remote host by OID using SNMPv2 on a specified port

```bash
snmpwalk -v 2c -c community ip:port oid
```

### Query system information on a remote host by OID using SNMPv3 and authentication without encryption

```bash
snmpwalk -v 3 -l authNoPriv -u username -a MD5|SHA -A passphrase ip oid
```

### Query system information on a remote host by OID using SNMPv3, authentication, and encryption

```bash
snmpwalk -v 3 -l authPriv -u username -a MD5|SHA -A auth_passphrase -x DES|AES -X enc_passphrase ip oid
```

### Query system information on a remote host by OID using SNMPv3 without authentication or encryption

```bash
snmpwalk -v 3 -l noAuthNoPriv -u username ip oid
```

### Display help

```bash
snmpwalk [-h|--help]
```
