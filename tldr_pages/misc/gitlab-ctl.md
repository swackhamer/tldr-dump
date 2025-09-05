# gitlab-ctl

> Manage the GitLab omnibus. More information: <https://docs.gitlab.com/omnibus/maintenance/>.

## Examples

### Display the status of every service

```bash
sudo gitlab-ctl status
```

### Display the status of a specific service

```bash
sudo gitlab-ctl status nginx
```

### Restart every service

```bash
sudo gitlab-ctl restart
```

### Restart a specific service

```bash
sudo gitlab-ctl restart nginx
```

### Display the logs of every service and keep reading until `<Ctrl c>` is pressed

```bash
sudo gitlab-ctl tail
```

### Display the logs of a specific service

```bash
sudo gitlab-ctl tail nginx
```

### Send the SIGKILL signal to specific service

```bash
sudo gitlab-ctl kill nginx
```

### Reconfigure the application

```bash
sudo gitlab-ctl reconfigure
```
