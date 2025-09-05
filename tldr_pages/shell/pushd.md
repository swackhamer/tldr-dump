# pushd

> Place a directory on a stack so it can be accessed later. See also: `popd` to switch back to original directory and `dirs` to display directory stack contents. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-pushd>.

## Examples

### Switch to directory and push it on the stack

```bash
pushd path/to/directory
```

### Switch first and second directories on the stack

```bash
pushd
```

### Rotate stack by making the 5th element the top of the stack

```bash
pushd +4
```

### Rotate the stack 4 times to the left (the current directory stays at the top by replacing the 5th element)

```bash
pushd -n +4
```
