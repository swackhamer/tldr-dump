# mysides

> Add, list and remove finder favorites. More information: <https://github.com/mosen/mysides>.

## Examples

### List sidebar favorites

```bash
mysides list
```

### Add a new item to the end of the sidebar favorites

```bash
mysides add example file:///Users/Shared/example
```

### Remove an item by name

```bash
mysides remove example
```

### Add the current directory to the sidebar

```bash
mysides add $(basename $(pwd)) file:///$(pwd)
```

### Remove the current directory from the sidebar

```bash
mysides remove $(basename $(pwd))
```
