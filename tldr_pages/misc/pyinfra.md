# pyinfra

> Automates infrastructure at a large scale. More information: <https://docs.pyinfra.com>.

## Examples

### Execute a command over SSH

```bash
pyinfra target_ip_address exec -- command_name_and_arguments
```

### Execute contents of a deploy file on a list of targets

```bash
pyinfra path/to/target_list.py path/to/deploy.py
```

### Execute commands on locally

```bash
pyinfra @local path/to/deploy.py
```

### Execute commands over Docker

```bash
pyinfra @docker/container path/to/deploy.py
```
