# audit2allow

> Scan logs for messages pertaining to denied permissions. Generate a report of Type Enforcement (TE) rules that might allow successful operations. See also: `audit2why`. More information: <https://manned.org/audit2allow>.

## Examples

### Show all generated messages in audit and message logs

```bash
audit2allow [-a|--all]
```

### Show all generated messages since last boot

```bash
audit2allow [-b|--boot]
```

### Display detailed information around generated messages

```bash
audit2allow [-e|--explain]
```

### Enable verbose output mode

```bash
audit2allow [-v|--verbose]
```

### Use installed macros to generate a reference policy

```bash
audit2allow [-R|--reference]
```

### Specify a policy file for further analysis

```bash
audit2allow [-p|--policy] path/to/policyfile
```

### Limit analysis to messages with a type specified in `regex`

```bash
audit2allow [-t|--type] type_regex
```

### Display help

```bash
audit2allow [-h|--help]
```
