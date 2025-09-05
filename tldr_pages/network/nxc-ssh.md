# nxc-ssh

> Pentest and exploit SSH servers. See also: `hydra`. More information: <https://www.netexec.wiki/ssh-protocol>.

## Examples

### Spray the specified password against a list of usernames on the specified target

```bash
nxc ssh 192.168.178.2 [-u|--username] path/to/usernames.txt [-p|--password] password
```

### Search for valid credentials by trying out every combination in the specified lists of usernames and passwords

```bash
nxc ssh 192.168.178.2 [-u|--username] path/to/usernames.txt [-p|--password] path/to/passwords.txt
```

### Use the specified private key for authentication, using the supplied password as the key's passphrase

```bash
nxc ssh 192.186.178.2 [-u|--username] path/to/usernames.txt [-p|--password] password --key-file path/to/id_rsa
```

### Try a combination of username and password on a number of targets

```bash
nxc ssh 192.168.178.0/24 [-u|--username] username [-p|--password] password
```

### Check for `sudo` privileges on a successful login

```bash
nxc ssh 192.168.178.2 [-u|--username] username [-p|--password] path/to/passwords.txt --sudo-check
```
