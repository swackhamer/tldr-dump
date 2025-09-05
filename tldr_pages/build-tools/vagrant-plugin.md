# vagrant-plugin

> Manage Vagrant plugins. See also: `vagrant`. More information: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

## Examples

### List all the plugins currently installed

```bash
vagrant plugin list
```

### Install a plugin from remote repositories, usually RubyGems

```bash
vagrant plugin install vagrant_vbguest
```

### Install a plugin from a local file source

```bash
vagrant plugin install path/to/my_plugin.gem
```

### Update all installed plugins to their latest version

```bash
vagrant plugin update
```

### Update a plugin to the latest version

```bash
vagrant plugin update vagrant_vbguest
```

### Uninstall a specific plugin

```bash
vagrant plugin uninstall vagrant_vbguest
```
