# dokku

> Docker powered mini-Heroku (PaaS). Easily deploy multiple apps to your server in different languages using a single `git-push` command. More information: <https://dokku.com/docs/deployment/application-deployment/>.

## Examples

### List running apps

```bash
dokku apps
```

### Create an app

```bash
dokku apps:create app_name
```

### Remove an app

```bash
dokku apps:destroy app_name
```

### Install plugin

```bash
dokku plugin:install full_repo_url
```

### Link database to an app

```bash
dokku db:link db_name app_name
```
