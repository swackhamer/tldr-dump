# airpaste

> Share messages and files on the same network using mDNS. More information: <https://github.com/mafintosh/airpaste>.

## Examples

### Wait for a message and display it when received

```bash
airpaste
```

### Send text

```bash
echo text | airpaste
```

### Send a file

```bash
airpaste < path/to/file
```

### Receive a file

```bash
airpaste > path/to/file
```

### Create or join a channel

```bash
airpaste channel_name
```
