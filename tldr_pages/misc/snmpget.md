# snmpget

> Query using the SNMP protocol. More information: <https://manned.org/snmpget>.

## Examples

### Request a single value from the SNMP agent

```bash
snmpget -v version -c community ip oid
```

### Display the full Object Identifier (OID) path

```bash
snmpget -v version -c community -O f ip oid
```

### Display help

```bash
snmpget [-h|--help]
```
