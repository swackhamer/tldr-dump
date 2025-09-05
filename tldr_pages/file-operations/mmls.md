# mmls

> Display the partition layout of a volume system. More information: <https://wiki.sleuthkit.org/index.php?title=Mmls>.

## Examples

### Display the partition table stored in an image file

```bash
mmls path/to/image_file
```

### Display the partition table with an additional column for the partition size

```bash
mmls -B -i path/to/image_file
```

### Display the partition table in a split EWF image

```bash
mmls -i ewf image.e01 image.e02
```

### Display nested partition tables

```bash
mmls -t nested_table_type -o offset path/to/image_file
```
