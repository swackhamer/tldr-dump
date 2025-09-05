# odps-auth

> User authorities in ODPS (Open Data Processing Service). See also: `odps`. More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

## Examples

### Add a user to the current project

```bash
add user username;
```

### Grant a set of authorities to a user

```bash
grant action_list on object_type object_name to user username;
```

### Show authorities of a user

```bash
show grants for username;
```

### Create a user role

```bash
create role role_name;
```

### Grant a set of authorities to a role

```bash
grant action_list on object_type object_name to role role_name;
```

### Describe authorities of a role

```bash
desc role role_name;
```

### Grant a role to a user

```bash
grant role_name to username;
```
