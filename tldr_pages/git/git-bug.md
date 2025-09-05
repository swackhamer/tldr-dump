# git-bug

> A distributed bug tracker that uses Git's internal storage, so no files are added in your project. You may submit your problems to the same Git remote you use to interact with others, much like commits and branches. More information: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

## Examples

### Create a new identity

```bash
git bug user create
```

### Create a new bug

```bash
git bug add
```

### Push a new bug entry to a remote

```bash
git bug push
```

### Pull for updates

```bash
git bug pull
```

### List existing bugs

```bash
git bug ls
```

### Filter and sort bugs using a query

```bash
git bug ls "status:open sort:edit"
```

### Search for bugs by text content

```bash
git bug ls "search_query" baz
```
