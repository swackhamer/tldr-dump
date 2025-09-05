# kcadm.sh

> Perform administration tasks. More information: <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>.

## Examples

### Start an authenticated session

```bash
kcadm.sh config credentials --server host --realm realm_name --user username --password password
```

### Create a user

```bash
kcadm.sh create users -s username=username -r realm_name
```

### List all realms

```bash
kcadm.sh get realms
```

### Update a realm with JSON config

```bash
kcadm.sh update realms/realm_name -f path/to/file.json
```
