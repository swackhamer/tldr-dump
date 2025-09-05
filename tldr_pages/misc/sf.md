# sf

> A powerful command-line interface that simplifies development and build automation when working with your Salesforce org. More information: <https://developer.salesforce.com/tools/salesforcecli>.

## Examples

### Authorize a Salesforce Organization

```bash
sf force:auth:web:login --setalias organization --instanceurl organization_url
```

### List all authorized organizations

```bash
sf force:org:list
```

### Open a specific organization in the default web browser

```bash
sf force:org:open --targetusername organization
```

### Display information about a specific organization

```bash
sf force:org:display --targetusername organization
```

### Push source metadata to an Organization

```bash
sf force:source:push --targetusername organization
```

### Pull source metadata from an Organization

```bash
sf force:source:pull --targetusername organization
```

### Generate a password for the organization's logged-in user

```bash
sf force:user:password:generate --targetusername organization
```

### Assign a permission set for the organization's logged-in user

```bash
sf force:user:permset:assign --permsetname permission_set_name --targetusername organization
```
