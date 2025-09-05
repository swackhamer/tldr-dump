# sc_tracediff

> Display traceroute paths where the path has changed. More information: <https://www.caida.org/catalog/software/scamper/>.

## Examples

### Show the difference between traceroutes in two `warts` files

```bash
sc_tracediff path/to/file1.warts path/to/file2.warts
```

### Show the difference between the traceroutes in two `warts` files, including those that have not changed

```bash
sc_tracediff -a path/to/file1.warts path/to/file2.warts
```

### Show the difference between the traceroutes in two `warts` files and try to show DNS names and not IP addresses if possible

```bash
sc_tracediff -n path/to/file1.warts path/to/file2.warts
```
