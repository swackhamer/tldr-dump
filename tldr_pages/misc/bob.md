# bob

> Manage and switch between Neovim versions. More information: <https://github.com/MordechaiHadad/bob>.

## Examples

### Install and switch to the specified version of Neovim

```bash
bob use nightly|stable|latest|version_string|commit_hash
```

### List installed and currently used versions of Neovim

```bash
bob list
```

### Uninstall the specified version of Neovim

```bash
bob uninstall nightly|stable|latest|version_string|commit_hash
```

### Uninstall Neovim and erase any changes `bob` has made

```bash
bob erase
```

### Roll back to a previous nightly version

```bash
bob rollback
```
