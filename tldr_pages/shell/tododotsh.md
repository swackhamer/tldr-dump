# todo.sh

> Simple and extensible shell script for managing your `todo.txt` file. More information: <https://github.com/todotxt/todo.txt-cli>.

## Examples

### List every item

```bash
todo.sh ls
```

### Add an item with project and context tags

```bash
todo.sh add 'description +project @context'
```

### Mark an item as [do]ne

```bash
todo.sh do item_no
```

### Remove an item

```bash
todo.sh rm item_no
```

### Set an item's [pri]ority (A-Z)

```bash
todo.sh pri item_no priority
```

### Replace an item

```bash
todo.sh replace item_no 'new_description'
```
