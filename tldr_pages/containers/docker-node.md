# docker-node

> Manage Docker Swarm nodes. More information: <https://docs.docker.com/reference/cli/docker/node/>.

## Examples

### List nodes in the swarm

```bash
docker node ls
```

### List tasks running on one or more nodes, defaults to the current node

```bash
docker node ps node1 node2 node3 ...
```

### Display detailed information on one or more nodes

```bash
docker node inspect node1 node2 node3 ...
```

### Promote one or more nodes to manager in the swarm

```bash
docker node promote node1 node2 node3 ...
```

### Demote one or more nodes from manager in the swarm

```bash
docker node demote node1 node2 node3 ...
```

### Remove one or more nodes from the swarm

```bash
docker node rm node1 node2 node3 ...
```

### Update metadata about a node, such as its availability, labels, or roles

```bash
docker node update --availability|role|label-add|... active|worker|foo|... node1
```
