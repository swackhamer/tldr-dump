# odps-func

> Manage functions in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Show functions in the current project

```bash
list functions;
```

### Create a Java function using a `.jar` resource

```bash
create function func_name as path.to.package.Func using 'package.jar';
```

### Create a Python function using a `.py` resource

```bash
create function func_name as script.Func using 'script.py';
```

### Delete a function

```bash
drop function func_name;
```
