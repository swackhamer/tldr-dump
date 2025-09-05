# git-gui

> A GUI for Git to manage branches, commits, and remotes, and perform local merges. See also: `git-cola`, `gitk`. More information: <https://git-scm.com/docs/git-gui>.

## Examples

### Launch the GUI

```bash
git gui
```

### Show a specific file with author name and commit hash on each line

```bash
git gui blame path/to/file
```

### Open `git gui blame` in a specific revision

```bash
git gui blame revision path/to/file
```

### Open `git gui blame` and scroll the view to center on a specific line

```bash
git gui blame --line=line path/to/file
```

### Open a window to make one commit and return to the shell when it is complete

```bash
git gui citool
```

### Open `git gui citool` in the "Amend Last Commit" mode

```bash
git gui citool --amend
```

### Open `git gui citool` in a read-only mode

```bash
git gui citool --nocommit
```

### Show a browser for the tree of a specific branch, opening the blame tool when clicking on the files

```bash
git gui browser maint
```
