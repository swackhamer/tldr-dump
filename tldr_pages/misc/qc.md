# qc

> Manage and execute command snippets stored in QOwnNotes notes. See also: `qownnotes`. More information: <https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

## Examples

### Configure the snippet manager, e.g. to set the security token from QOwnNotes

```bash
qc configure
```

### Search and print command snippets stored in your `Commands.md` note and all your notes tagged with `commands`

```bash
qc search
```

### Execute a snippet and show the command before executing

```bash
qc exec --command
```

### Execute the last snippet and show the command before executing

```bash
qc exec --command --last
```

### Switch between note folders in QOwnNotes

```bash
qc switch
```
