# yadm-config

> Pass options to `yadm`'s config file. Change the `.config` of the repository managed by `yadm`. More information: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

## Examples

### Set or update a `yadm`'s Git configuration

```bash
yadm config key.inner-key value
```

### Get a value from `yadm`'s Git configuration

```bash
yadm config --get key
```

### Unset a value in `yadm`'s Git configuration

```bash
yadm config --unset key
```

### List all values in `yadm`'s Git configuration

```bash
yadm config --list
```
