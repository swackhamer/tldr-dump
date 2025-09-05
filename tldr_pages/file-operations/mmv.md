# mmv

> Move and rename files in bulk. More information: <https://manned.org/mmv.1>.

## Examples

### Rename all files with a certain extension to a different extension

```bash
mmv "*.old_extension" "#1.new_extension"
```

### Copy `report6part4.txt` to `./french/rapport6partie4.txt` along with all similarly named files

```bash
mmv [-c|--copy] "report*part*.txt" "./french/rapport#1partie#2.txt"
```

### Append all `.txt` files into one file

```bash
mmv [-a|--append] "*.txt" "all.txt"
```

### Convert dates in filenames from "M-D-Y" format to "D-M-Y" format

```bash
mmv "[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt" "#3#4-#1#2-#5#6#7#8.txt"
```
