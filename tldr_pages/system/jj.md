# jj

> Jujutsu, a version control system. Some subcommands such as `log`, `desc`, `new`, `git`, etc. have their own usage documentation. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/>.

## Examples

### Update description of the revisions specified by given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.)

```bash
jj [desc|describe] [-m|--message] "message" [-r|--revision] revsets
```

### Create a new commit/revision on top of a given revision

```bash
jj new revset
```

### Create a new merge commit on top of multiple revisions

```bash
jj new revset1 revset2 ...
```

### Update the working copy to point to a revision

```bash
jj edit revset
```

### Undo the previous command (which may itself have been `undo`)

```bash
jj undo
```

### Execute a jj subcommand without snapshotting the working copy

```bash
jj --ignore-working-copy subcommand
```

### Execute a jj subcommand at an operation

```bash
jj [--at-op|--at-operation] operation subcommand
```

### Display help for a specific subcommand (like `new`, `commit`, `desc`, etc.)

```bash
jj help subcommand
```
