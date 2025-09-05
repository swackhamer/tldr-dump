# dolt-gc

> Search the repository for data that are no longer referenced and no longer needed. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-gc>.

## Examples

### Clean up unreferenced data from the repository

```bash
dolt gc
```

### Initiate a faster but less thorough garbage collection process

```bash
dolt gc [-s|--shallow]
```
