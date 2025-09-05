# mesg

> Check or set a terminal's ability to receive messages from other users, usually from the `write` command. See also: `write`, `talk`. More information: <https://manned.org/mesg.1p>.

## Examples

### Check terminal's openness to write messages

```bash
mesg
```

### Disallow receiving messages from the write command

```bash
mesg n
```

### Allow receiving messages from the write command

```bash
mesg y
```
