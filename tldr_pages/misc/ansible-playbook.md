# ansible-playbook

> Execute tasks defined in playbook on remote machines over SSH. More information: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

## Examples

### Run tasks in playbook

```bash
ansible-playbook playbook
```

### Run tasks in playbook with custom host inventory

```bash
ansible-playbook playbook [-i|--inventory] inventory_file
```

### Run tasks in playbook with extra variables defined via the command-line

```bash
ansible-playbook playbook [-e|--extra-vars] "variable1=value1 variable2=value2"
```

### Run tasks in playbook with extra variables defined in a JSON file

```bash
ansible-playbook playbook [-e|--extra-vars] "@variables.json"
```

### Run tasks in playbook for the given tags

```bash
ansible-playbook playbook [-t|--tags] tag1,tag2
```

### Run tasks in a playbook starting at a specific task

```bash
ansible-playbook playbook --start-at task_name
```

### Run tasks in a playbook without making any changes (dry-run)

```bash
ansible-playbook playbook [-C|--check] [-D|--diff]
```
