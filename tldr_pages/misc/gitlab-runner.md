# gitlab-runner

> Manage GitLab runners. More information: <https://docs.gitlab.com/runner/>.

## Examples

### Register a runner

```bash
sudo gitlab-runner register --url https://gitlab.example.com --registration-token token --name name
```

### Register a runner with a Docker executor

```bash
sudo gitlab-runner register --url https://gitlab.example.com --registration-token token --name name --executor docker
```

### Unregister a runner

```bash
sudo gitlab-runner unregister --name name
```

### Display the status of the runner service

```bash
sudo gitlab-runner status
```

### Restart the runner service

```bash
sudo gitlab-runner restart
```

### Check if the registered runners can connect to GitLab

```bash
sudo gitlab-runner verify
```
