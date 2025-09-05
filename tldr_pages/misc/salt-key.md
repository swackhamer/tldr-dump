# salt-key

> Manage salt minion keys on the salt master. Needs to be run on the salt master, likely as root or with sudo. More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>.

## Examples

### List all accepted, unaccepted and rejected minion keys

```bash
salt-key [-L|--list-all]
```

### Accept a minion key by name

```bash
salt-key [-a|--accept-all] MINION_ID
```

### Reject a minion key by name

```bash
salt-key [-r|--reject] MINION_ID
```

### Print fingerprints of all public keys

```bash
salt-key [-F|--finger-all]
```
