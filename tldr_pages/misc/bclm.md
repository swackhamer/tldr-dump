# bclm

> Set a custom charge limit on MacBooks. More information: <https://github.com/zackelia/bclm>.

## Examples

### Set the charge limit to about 80% (for Intel machines, the battery charge level may be slightly lower than the set value)

```bash
sudo bclm write 77
```

### Read the current charge limit

```bash
bclm read
```

### Keep the charge limit after rebooting/smc reset

```bash
sudo bclm persist
```

### Remove the persistent charge limit

```bash
sudo bclm unpersist
```
