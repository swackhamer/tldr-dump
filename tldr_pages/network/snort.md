# snort

> Open-source network intrusion detection system. More information: <https://www.snort.org/#documents>.

## Examples

### Capture packets with verbose output

```bash
sudo snort -v -i interface
```

### Capture packets and dump application layer data with verbose output

```bash
sudo snort -vd -i interface
```

### Capture packets and display link layer packet headers with verbose output

```bash
sudo snort -ve -i interface
```

### Capture packets and save them in the specified directory

```bash
sudo snort -i interface -l path/to/directory
```

### Capture packets according to rules and save offending packets along with alerts

```bash
sudo snort -i interface -c path/to/rules.conf -l path/to/directory
```
