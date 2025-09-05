# snmpgetnext

> Query the next value in the MIB tree. More information: <https://manned.org/snmpgetnext>.

## Examples

### Request the next value from the SNMP agent

```bash
snmpgetnext -v version -c community ip oid
```

### Display the full Object Identifier (OID) path

```bash
snmpgetnext -v version -c community -O f ip oid
```

### Display help

```bash
snmpgetnext [-h|--help]
```
