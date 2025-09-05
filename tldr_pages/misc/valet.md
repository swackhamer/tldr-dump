# valet

> A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`. More information: <https://laravel.com/docs/valet>.

## Examples

### Start the valet daemon

```bash
valet start
```

### Register the current working directory as a path that Valet should search for sites

```bash
valet park
```

### View 'parked' paths

```bash
valet paths
```

### Serve a single site instead of an entire directory

```bash
valet link application_name
```

### Share a project via an Ngrok tunnel

```bash
valet share
```
