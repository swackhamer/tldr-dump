# docker-swarm

> A container orchestration tool. More information: <https://docs.docker.com/engine/swarm/>.

## Examples

### Initialize a swarm cluster

```bash
docker swarm init
```

### Display the token to join a manager or a worker

```bash
docker swarm join-token worker|manager
```

### Join a new node to the cluster

```bash
docker swarm join --token token manager_node_url:2377
```

### Remove a worker from the swarm (run inside the worker node)

```bash
docker swarm leave
```

### Display the current CA certificate in PEM format

```bash
docker swarm ca
```

### Rotate the current CA certificate and display the new certificate

```bash
docker swarm ca --rotate
```

### Change the valid period for node certificates

```bash
docker swarm update --cert-expiry hourshminutesmsecondss
```
