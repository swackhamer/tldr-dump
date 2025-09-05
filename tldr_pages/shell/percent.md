# %

> Manage jobs. More information: <https://www.gnu.org/software/bash/manual/bash.html#Job-Control-Basics>.

## Examples

### Bring the current job to front

```bash
%
```

### Bring the previous job to front

```bash
%-
```

### Bring the job number `n` to front

```bash
%n
```

### Bring a job whose command starts with `string` to front

```bash
%string
```

### Bring a job whose command contains `string` to front

```bash
%?string
```

### Resume a suspended job

```bash
%1 &
```
