# gnmic-set

> Modify gnmi network device configuration. More information: <https://gnmic.kmrd.dev/cmd/set>.

## Examples

### Update the value of a path

```bash
gnmic [-a|--address] ip:port set --update-path path --update-value value
```

### Update the value of a path to match the contents of a JSON file

```bash
gnmic [-a|--address] ip:port set --update-path path --update-file filepath
```

### Replace the value of a path to match the contents of a JSON file

```bash
gnmic [-a|--address] ip:port set --replace-path path --replace-file filepath
```

### Delete the node at a given path

```bash
gnmic [-a|--address] ip:port set --delete path
```
