# nms

> Tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers from `stdin`. More information: <https://github.com/bartobri/no-more-secrets>.

## Examples

### Decrypt text after a keystroke

```bash
echo "Hello, World!" | nms
```

### Decrypt output immediately, without waiting for a keystroke

```bash
ls -la | nms -a
```

### Decrypt the content of a file, with a custom output color

```bash
cat path/to/file | nms -a -f blue|white|yellow|black|magenta|green|red
```

### Clear the screen before decrypting

```bash
command | nms -a -c
```
