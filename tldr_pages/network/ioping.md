# ioping

> Monitor I/O latency in real time. More information: <https://github.com/koct9i/ioping>.

## Examples

### Show disk I/O latency using the default values and the current directory

```bash
ioping .
```

### Measure latency on /tmp using 10 requests of 1 megabyte each

```bash
ioping [-c|-count] 10 [-s|-size] 1M /tmp
```

### Measure disk seek rate on `/dev/sdX`

```bash
ioping [-R|-rapid] /dev/sdX
```

### Measure disk sequential speed on `/dev/sdX`

```bash
ioping [-RL|-rapid -linear] /dev/sdX
```
