# git-count-objects

> Count the number of unpacked objects and their disk consumption. More information: <https://git-scm.com/docs/git-count-objects>.

## Examples

### Count all objects and display the total disk usage

```bash
git count-objects
```

### Display a count of all objects and their total disk usage, displaying sizes in human-readable units

```bash
git count-objects [-H|--human-readable]
```

### Display more verbose information

```bash
git count-objects [-v|--verbose]
```

### Display more verbose information, displaying sizes in human-readable units

```bash
git count-objects [-H|--human-readable] [-v|--verbose]
```
