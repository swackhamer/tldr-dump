# heroku

> Create and manage Heroku apps. More information: <https://devcenter.heroku.com/articles/heroku-cli#get-started-with-the-heroku-cli>.

## Examples

### Log in to your Heroku account

```bash
heroku login
```

### Create a Heroku app

```bash
heroku create
```

### Show logs for an app

```bash
heroku logs --app app_name
```

### Run a one-off process inside a dyno (Heroku virtual machine)

```bash
heroku run process_name --app app_name
```

### List dynos (Heroku virtual machines) for an app

```bash
heroku ps --app app_name
```

### Permanently destroy an app

```bash
heroku destroy --app app_name
```
