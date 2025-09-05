# sntp

> A very Simple Network Time Protocol client program. More information: <https://keith.github.io/xcode-man-pages/sntp.1>.

## Examples

### Query a specified SNTP server and display the time

```bash
sntp pool.ntp.org
```

### Synchronize the system clock with a specified SNTP server

```bash
sudo sntp -S pool.ntp.org
```

### Enable debug logging

```bash
sntp -d pool.ntp.org
```
