# erl

> Run and manage programs in the Erlang programming language. More information: <https://www.erlang.org>.

## Examples

### Compile and run sequential Erlang program as a common script and then exit

```bash
erlc path/to/file1 path/to/file2 ... && erl -noshell 'mymodule:myfunction(arguments), init:stop().'
```

### Connect to a running Erlang node

```bash
erl -remsh nodename@hostname -sname custom_shortname -hidden -setcookie cookie_of_remote_node
```

### Tell the Erlang shell to load modules from a directory

```bash
erl -pa path/to/directory_with_beam_files
```
