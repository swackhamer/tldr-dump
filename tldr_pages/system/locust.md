# locust

> Load-testing tool to determine number of concurrent users a system can handle. More information: <https://locust.io>.

## Examples

### Load-test "example.com" with web interface using locustfile.py

```bash
locust --host=http://example.com
```

### Use a different test file

```bash
locust --locustfile=test_file.py --host=http://example.com
```

### Run test without web interface, spawning 1 user a second until there are 100 users

```bash
locust --no-web --clients=100 --hatch-rate=1 --host=http://example.com
```

### Start Locust in master mode

```bash
locust --master --host=http://example.com
```

### Connect Locust slave to master

```bash
locust --slave --host=http://example.com
```

### Connect Locust slave to master on a different machine

```bash
locust --slave --master-host=master_hostname --host=http://example.com
```
