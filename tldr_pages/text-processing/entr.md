# entr

> Run arbitrary commands when files change. More information: <https://eradman.com/entrproject/>.

## Examples

### Rebuild with `make` if any file in any subdirectory changes

```bash
ag --files-with-matches | entr make
```

### Rebuild and test with `make` if any `.c` source files in the current directory change

```bash
ls *.c | entr 'make && make test'
```

### Send a `SIGTERM` to any previously spawned ruby subprocesses before executing `ruby main.rb`

```bash
ls *.rb | entr -r ruby main.rb
```

### Run a command with the changed file (`/_`) as an argument

```bash
ls *.sql | entr psql -f /_
```

### [c]lear the screen and run a query after the SQL script is updated

```bash
echo my.sql | entr -cp psql -f /_
```

### Rebuild the project if source files change, limiting output to the first few lines

```bash
find src/ | entr -s 'make | sed 10q'
```

### Launch and auto-[r]eload a Node.js server

```bash
ls *.js | entr -r node app.js
```
