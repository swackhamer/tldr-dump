# jmeter

> Open source Java application designed for load testing functional behavior and measure performance. More information: <https://jmeter.apache.org>.

## Examples

### Run a specific test plan in nongui mode

```bash
jmeter --nongui --testfile path/to/file.jmx
```

### Run a test plan in nongui mode using a specific log file

```bash
jmeter --nogui --testfile path/to/file.jmx --logfile path/to/logfile.jtl
```

### Run a test plan in nongui mode using a specific proxy

```bash
jmeter --nongui --testfile path/to/file.jmx --proxyHost 127.0.0.1 --proxyPort 8888
```

### Run a test plan in nongui mode using a specific JMeter property

```bash
jmeter --jmeterproperty key='value' --nongui --testfile path/to/file.jmx
```
