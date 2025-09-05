# perlbrew

> Manage Perl installations in the home directory. See also: `asdf`. More information: <https://github.com/gugod/App-perlbrew>.

## Examples

### Initialize a `perlbrew` environment

```bash
perlbrew init
```

### List available Perl versions

```bash
perlbrew available
```

### Install/uninstall a Perl version

```bash
perlbrew install|uninstall version
```

### List perl installations

```bash
perlbrew list
```

### Switch to an installation and set it as default

```bash
perlbrew switch perl-version
```

### Use the system Perl again

```bash
perlbrew off
```

### List installed CPAN modules for the installation in use

```bash
perlbrew list-modules
```

### Clone CPAN modules from one installation to another

```bash
perlbrew clone-modules source_installation destination_installation
```
