# redis-benchmark

> Benchmark a Redis server. More information: <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>.

## Examples

### Run full benchmark

```bash
redis-benchmark
```

### Run benchmark on a specific Redis server

```bash
redis-benchmark -h host -p port -a password
```

### Run a subset of tests with default 100000 requests

```bash
redis-benchmark -h host -p port -t set,lpush -n 100000
```

### Run with a specific script

```bash
redis-benchmark -n 100000 script load "redis.call('set', 'foo', 'bar')"
```

### Run benchmark by using 100000 [r]andom keys

```bash
redis-benchmark -t set -r 100000
```

### Run benchmark by using a [P]ipelining of 16 commands

```bash
redis-benchmark -n 1000000 -t set,get -P 16
```

### Run benchmark [q]uietly and only show query per seconds result

```bash
redis-benchmark -q
```
