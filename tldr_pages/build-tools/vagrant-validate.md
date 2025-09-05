# vagrant-validate

> Check the validity of a Vagrantfile. See also: `vagrant`, `vagrant box`, `vagrant plugin`. More information: <https://developer.hashicorp.com/vagrant/docs/cli/validate>.

## Examples

### Validate the syntax of the Vagrantfile to ensure it is correctly structured and free of errors

```bash
vagrant validate
```

### Ensure that the Vagrantfile is correctly structured while ignoring provider-specific configuration options

```bash
vagrant validate [-p|--ignore-provider] docker|hypervlibvirt|parallels|qemu|virtualbox|vmware_desktop
```
