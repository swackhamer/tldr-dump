# yadm-gitconfig

> Pass options to `git config`. Change the `.gitconfig` of the repository managed by `yadm`. See also: `git config`. More information: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

## Examples

### Update or set a Git configuration value

```bash
yadm gitconfig key.inner-key value
```

### Get a value from `yadm`'s Git configuration

```bash
yadm gitconfig --get key
```

### Unset a value in `yadm`'s Git configuration

```bash
yadm gitconfig --unset key
```

### List all values in `yadm`'s Git configuration

```bash
yadm gitconfig --list
```
