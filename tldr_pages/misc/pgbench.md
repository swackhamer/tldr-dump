# pgbench

> Run a benchmark test on PostgreSQL. More information: <https://www.postgresql.org/docs/current/pgbench.html>.

## Examples

### Initialize a database with a scale factor of 50 times the default size

```bash
pgbench --initialize --scale=50 database_name
```

### Benchmark a database with 10 clients, 2 worker threads, and 10,000 transactions per client

```bash
pgbench --client=10 --jobs=2 --transactions=10000 database_name
```
