# vagrant-halt

> Shuts down the running machine Vagrant is managing. See also: `vagrant`, `vagrant box`, `vagrant plugin`, `vagrant validate`. More information: <https://developer.hashicorp.com/vagrant/docs/cli/halt>.

## Examples

### Halt the currently running Vagrant machine gracefully

```bash
vagrant halt
```

### Halt a specific machine by its ID or name gracefully

```bash
vagrant halt id_or_name
```

### Forcefully halt the current running machine(s) (This can affect multiple running machines if they are part of the same Vagrant environment)

```bash
vagrant halt [-f|--force]
```

### Forcefully halt a specific machine by its ID or name

```bash
vagrant halt [-f|--force] id_or_name
```
