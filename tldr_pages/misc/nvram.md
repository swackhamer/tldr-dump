# nvram

> Manipulate firmware variables. More information: <https://keith.github.io/xcode-man-pages/nvram.8.html>.

## Examples

### [p]rint all the variables stored in the NVRAM

```bash
nvram -p
```

### [p]rint all the variables stored in the NVRAM using [x]ML format

```bash
nvram -xp
```

### Modify the value of a firmware variable

```bash
sudo nvram name="value"
```

### [d]elete a firmware variable

```bash
sudo nvram -d name
```

### [c]lear all the firmware variables

```bash
sudo nvram -c
```

### Set a firmware variable from a specific [x]ML [f]ile

```bash
sudo nvram -xf path/to/file.xml
```
