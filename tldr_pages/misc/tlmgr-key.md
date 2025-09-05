# tlmgr-key

> Manage GPG keys used to verify TeX Live databases. More information: <https://www.tug.org/texlive/doc/tlmgr.html#key>.

## Examples

### List all keys for TeX Live

```bash
tlmgr key list
```

### Add a key from a specific file

```bash
sudo tlmgr key add path/to/key.gpg
```

### Add a key from `stdin`

```bash
cat path/to/key.gpg | sudo tlmgr key add -
```

### Remove a specific key by its ID

```bash
sudo tlmgr key remove key_id
```
