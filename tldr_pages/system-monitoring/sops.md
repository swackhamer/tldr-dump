# sops

> SOPS (Secrets OPerationS): a simple and flexible tool for managing secrets. More information: <https://github.com/getsops/sops>.

## Examples

### Encrypt a file

```bash
sops -e path/to/file.json > path/to/file.enc.json
```

### Decrypt a file to `stdout`

```bash
sops -d path/to/file.enc.json
```

### Update the declared keys in a `sops` file

```bash
sops updatekeys path/to/file.enc.yaml
```

### Rotate data keys for a `sops` file

```bash
sops -r path/to/file.enc.yaml
```

### Change the extension of the file once encrypted

```bash
sops -d --input-type json path/to/file.enc.json
```

### Extract keys by naming them, and array elements by numbering them

```bash
sops -d --extract '["an_array"][1]' path/to/file.enc.json
```

### Show the difference between two `sops` files

```bash
diff <(sops -d path/to/secret1.enc.yaml) <(sops -d path/to/secret2.enc.yaml)
```
