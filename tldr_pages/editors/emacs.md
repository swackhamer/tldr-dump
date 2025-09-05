# emacs

> The extensible, customizable, self-documenting, real-time display editor. See also: `emacsclient`. More information: <https://www.gnu.org/software/emacs>.

## Examples

### Start Emacs and open a file

```bash
emacs path/to/file
```

### Open a file at a specified line number

```bash
emacs +line_number path/to/file
```

### Run an Emacs Lisp file as a script

```bash
emacs --script path/to/file.el
```

### Start Emacs in console mode (without an X window)

```bash
emacs [-nw|--no-window-system]
```

### Start an Emacs server in the background (accessible via `emacsclient`)

```bash
emacs --daemon
```

### Stop a running Emacs server and all its instances, asking for confirmation on unsaved files

```bash
emacsclient --eval '(save-buffers-kill-emacs)'
```

### Save a file in Emacs

```bash
<Ctrl x><Ctrl s>
```

### Quit Emacs

```bash
<Ctrl x><Ctrl c>
```
