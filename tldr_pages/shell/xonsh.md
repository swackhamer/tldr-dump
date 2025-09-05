# xonsh

> Python-powered, cross-platform, Unix-gazing shell. Write and mix sh/Python code in Xonsh (pronounced conch). More information: <https://xon.sh/contents.html>.

## Examples

### Start an interactive shell session

```bash
xonsh
```

### Execute a single command and then exit

```bash
xonsh -c "command"
```

### Run commands from a script file and then exit

```bash
xonsh path/to/script_file.xonsh
```

### Define environment variables for the shell process

```bash
xonsh -Dname1=value1 -Dname2=value2
```

### Load the specified `.xonsh` or `.json` configuration files

```bash
xonsh --rc path/to/file1.xonsh path/to/file2.json
```

### Skip loading the `.xonshrc` configuration file

```bash
xonsh --no-rc
```
