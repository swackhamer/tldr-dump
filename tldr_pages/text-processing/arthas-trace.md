# arthas-trace

> Trace method invoke chain, and output the time cost for each node in the path. See also: `arthas`, `arthas-watch`. More information: <https://arthas.aliyun.com/en/doc/trace.html>.

## Examples

### Trace method invoke chain

```bash
trace class-pattern method-pattern
```

### Trace method invoke chains and only display invoke information longer than 10 ms

```bash
trace class-pattern method-pattern '#cost > 10'
```

### Trace the invoke chain of multiple classes or multiple methods

```bash
trace -E class-pattern1|class-patter2 method-pattern1|method-pattern2|method-pattern3
```

### Track method invoke chains, only display invoke information that exceeds 10 ms, and exit after 5 times

```bash
trace class-pattern method-pattern '#cost > 10' -n 5
```
