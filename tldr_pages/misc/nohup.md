# nohup

> Allows for a process to live when the terminal gets killed. More information: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

## Examples

### Run a process that can live beyond the terminal

```bash
nohup command argument1 argument2 ...
```

### Launch `nohup` in background mode

```bash
nohup command argument1 argument2 ... &
```

### Run a shell script that can live beyond the terminal

```bash
nohup path/to/script.sh &
```

### Run a process and write the output to a specific file

```bash
nohup command argument1 argument2 ... > path/to/output_file &
```
