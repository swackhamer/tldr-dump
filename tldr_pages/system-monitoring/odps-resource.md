# odps-resource

> Manage resources in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Show resources in the current project

```bash
list resources;
```

### Add file resource

```bash
add file filename as alias;
```

### Add archive resource

```bash
add archive archive.tar.gz as alias;
```

### Add .jar resource

```bash
add jar package.jar;
```

### Add .py resource

```bash
add py script.py;
```

### Delete resource

```bash
drop resource resource_name;
```
