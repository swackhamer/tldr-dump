# vagrant

> Manage lightweight, reproducible, and portable development environments. Some subcommands such as `box`, `snapshot`, `halt`, etc. have their own usage documentation. More information: <https://developer.hashicorp.com/vagrant/docs/cli>.

## Examples

### Create a `Vagrantfile` in the current directory with the base Vagrant box

```bash
vagrant init
```

### Create a `Vagrantfile` with a box from the Vagrant Public Registry

```bash
vagrant init ubuntu/focal64
```

### Start and provision the Vagrant environment

```bash
vagrant up
```

### Suspend the machine

```bash
vagrant suspend
```

### Halt the machine

```bash
vagrant halt
```

### Connect to the machine via SSH

```bash
vagrant ssh
```

### Output the SSH configuration file of the running Vagrant machine

```bash
vagrant ssh-config
```

### List all local boxes

```bash
vagrant box list
```
