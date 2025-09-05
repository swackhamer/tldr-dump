# tig

> A configurable `ncurses`-based TUI for Git. See also: `gitui`, `git-gui`. More information: <https://jonas.github.io/tig/doc/manual.html>.

## Examples

### Show the sequence of commits starting from the current one in reverse chronological order

```bash
tig
```

### Show the history of a specific branch

```bash
tig branch
```

### Show the history of specific files or directories

```bash
tig path1 path2 ...
```

### Show the difference between two references (such as branches or tags)

```bash
tig base_ref..compared_ref
```

### Browse git blame interactively (press `<,>` to jump to parent)

```bash
tig blame path/to/file
```

### Display commits from all branches and stashes

```bash
tig --all
```

### Start in stash view, displaying all saved stashes

```bash
tig stash
```

### Display help in TUI

```bash
<h>
```
