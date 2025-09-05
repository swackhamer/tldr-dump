# tlmgr-generate

> Remake configuration files from information stored locally. More information: <https://www.tug.org/texlive/doc/tlmgr.html#generate>.

## Examples

### Remake the configuration file storing into a specific location

```bash
tlmgr generate --dest output_file
```

### Remake the configuration file using a local configuration file

```bash
tlmgr generate --localcfg local_configuration_file
```

### Run necessary programs after rebuilding configuration files

```bash
tlmgr generate --rebuild-sys
```
