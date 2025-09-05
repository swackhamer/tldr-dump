# argocd

> Interface to control an Argo CD server. Some subcommands such as `app` have their own usage documentation. More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

## Examples

### Login to Argo CD server

```bash
argocd login --insecure --username user --password password argocd_server:port
```

### List applications

```bash
argocd app list
```
