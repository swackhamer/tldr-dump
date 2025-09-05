# ansible-lint

> Apply rules and follow best practices with your automation content. More information: <https://ansible.readthedocs.io/projects/lint/>.

## Examples

### Lint a specific playbook and a role directory

```bash
ansible-lint path/to/playbook_file path/to/role_directory
```

### Lint a playbook while excluding specific rules

```bash
ansible-lint [-x|--exclude-rules] rule1,rule2,... path/to/playbook_file
```

### Lint a playbook in offline mode and format output as PEP8

```bash
ansible-lint [-o|--offline] [-p|--parseable] path/to/playbook_file
```

### Lint a playbook using a custom rules directory

```bash
ansible-lint [-r|--rules] path/to/custom_rules_directory path/to/playbook_file
```

### Lint all Ansible content recursively in a given directory

```bash
ansible-lint path/to/project_directory
```
