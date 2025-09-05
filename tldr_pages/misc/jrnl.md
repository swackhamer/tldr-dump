# jrnl

> A simple journal application. More information: <https://jrnl.sh>.

## Examples

### Insert a new entry with your editor

```bash
jrnl
```

### Quickly insert a new entry

```bash
jrnl today at 3am: title. content
```

### View the last ten entries

```bash
jrnl -n 10
```

### View everything that happened from the start of last year to the start of last march

```bash
jrnl -from "last year" -until march
```

### Edit all entries tagged with "texas" and "history"

```bash
jrnl @texas -and @history --edit
```
