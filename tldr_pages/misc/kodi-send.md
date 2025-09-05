# kodi-send

> Send actions to Kodi. More information: <https://kodi.wiki/view/List_of_built-in_functions>.

## Examples

### Quit Kodi

```bash
kodi-send [-a|--action] Quit
```

### Reboot the system

```bash
kodi-send [-a|--action] Reboot
```

### Send an action to a remote host

```bash
kodi-send --host 192.168.0.1 --port 9777 [-a|--action] Quit
```
