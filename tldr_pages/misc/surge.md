# surge

> Simple web publishing. More information: <https://surge.sh>.

## Examples

### Upload a new site to surge.sh

```bash
surge path/to/my_project
```

### Deploy site to custom domain (note that the DNS records must point to the surge.sh subdomain)

```bash
surge path/to/my_project my_custom_domain.com
```

### List your surge projects

```bash
surge list
```

### Remove a project

```bash
surge teardown my_custom_domain.com
```
