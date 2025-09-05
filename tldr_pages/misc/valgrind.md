# valgrind

> Wrapper for a set of expert tools for profiling, optimizing and debugging programs. Commonly used tools include `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind`, and `drd`. More information: <https://www.valgrind.org>.

## Examples

### Use the (default) Memcheck tool to show a diagnostic of memory usage by `program`

```bash
valgrind program
```

### Use Memcheck to report all possible memory leaks of `program` in full detail

```bash
valgrind --leak-check=full --show-leak-kinds=all program
```

### Use the Cachegrind tool to profile and log CPU cache operations of `program`

```bash
valgrind --tool=cachegrind program
```

### Use the Massif tool to profile and log heap memory and stack usage of `program`

```bash
valgrind --tool=massif --stacks=yes program
```
