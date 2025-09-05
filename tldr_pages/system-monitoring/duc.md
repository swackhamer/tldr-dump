# duc

> A collection of tools for indexing, inspecting, and visualizing disk usage. Duc maintains a database of accumulated sizes of directories of the file system, allowing queries in this database, or creating fancy graphs to show where data is. More information: <http://duc.zevv.nl>.

## Examples

### Index the `/usr` directory, writing to the default database location `~/.duc.db`

```bash
duc index /usr
```

### List all files and directories under `/usr/local`, showing relative file sizes in a graph

```bash
duc ls [-Fg|--classify --graph] /usr/local
```

### List all files and directories under `/usr/local` using treeview recursively

```bash
duc ls [-Fg|--classify --graph] [-R|--recursive] /usr/local
```

### Start the graphical interface to explore the file system using sunburst graphs

```bash
duc gui /usr
```

### Run the ncurses console interface to explore the file system

```bash
duc ui /usr
```

### Dump database info

```bash
duc info
```
