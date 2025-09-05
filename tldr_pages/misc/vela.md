# vela

> Tools for the Vela pipeline. More information: <https://go-vela.github.io/docs/reference/cli/>.

## Examples

### Trigger a pipeline to run from a Git branch, commit or tag

```bash
vela add deployment --org organization --repo repository_name --target environment --ref branch|commit|refs/tags/git_tag --description "deploy_description"
```

### List deployments for a repository

```bash
vela get deployment --org organization --repo repository_name
```

### Inspect a specific deployment

```bash
vela view deployment --org organization --repo repository_name --deployment deployment_number
```
