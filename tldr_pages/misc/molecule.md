# molecule

> Molecule helps testing Ansible roles. More information: <https://molecule.readthedocs.io>.

## Examples

### Create a new Ansible role

```bash
molecule init role --role-name role_name
```

### Run tests

```bash
molecule test
```

### Start the instance

```bash
molecule create
```

### Configure the instance

```bash
molecule converge
```

### List scenarios of the instance

```bash
molecule matrix converge
```

### Log in into the instance

```bash
molecule login
```
