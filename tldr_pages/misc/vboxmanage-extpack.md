# vboxmanage-extpack

> Manage extension packs for Oracle VirtualBox. More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>.

## Examples

### Install extension packs to VirtualBox (Note: You need to remove the existing version of the extension pack before installing a new version.)

```bash
VBoxManage extpack install path/to/file.vbox-extpack
```

### Remove the existing version of the VirtualBox extension pack

```bash
VBoxManage extpack install --replace
```

### Uninstall extension packs from VirtualBox

```bash
VBoxManage extpack uninstall extension_pack_name
```

### Uninstall extension packs and skip most uninstallation refusals

```bash
VBoxManage extpack uninstall --force extension_pack_name
```

### Clean up temporary files and directories left by extension packs

```bash
VBoxManage extpack cleanup
```
