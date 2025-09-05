# var-dump-server

> Symfony dump server. Collects data dumped by the Symfony VarDumper component. More information: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>.

## Examples

### Start the server

```bash
var-dump-server
```

### Dump the data in an HTML file

```bash
var-dump-server --format=html > path/to/file.html
```

### Make the server listen on a specific address and port

```bash
var-dump-server --host 127.0.0.1:9912
```
