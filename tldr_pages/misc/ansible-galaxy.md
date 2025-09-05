# ansible-galaxy

> Perform various Ansible Role and Collection related operations. More information: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

## Examples

### List installed roles or collections

```bash
ansible-galaxy role|collection list
```

### Search for a role with various levels of verbosely (`-v` should be specified at the end)

```bash
ansible-galaxy role search keyword -vvvvvv
```

### Install or remove role(s)

```bash
ansible-galaxy role install|remove role_name1 role_name2 ...
```

### Create a new role

```bash
ansible-galaxy role init role_name
```

### Get information about a role

```bash
ansible-galaxy role info role_name
```

### Install or remove collection(s)

```bash
ansible-galaxy collection install|remove collection_name1 collection_name2 ...
```

### Display help about roles or collections

```bash
ansible-galaxy role|collection [-h|--help]
```
