# odps-inst

> Manage instances in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Show instances created by current user

```bash
show instances;
```

### Describe the details of an instance

```bash
desc instance instance_id;
```

### Check the status of an instance

```bash
status instance_id;
```

### Wait on the termination of an instance, printing log and progress information until then

```bash
wait instance_id;
```

### Kill an instance

```bash
kill instance_id;
```
