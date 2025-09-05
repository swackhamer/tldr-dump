# stormlock

> Centralized locking system. More information: <https://github.com/tmccombs/stormlock>.

## Examples

### Acquire a lease for resource

```bash
stormlock acquire resource
```

### Release the given lease for the given resource

```bash
stormlock release resource lease_id
```

### Show information on the current lease for a resource, if any

```bash
stormlock current resource
```

### Test if a lease for given resource is currently active

```bash
stormlock is-held resource lease_id
```
