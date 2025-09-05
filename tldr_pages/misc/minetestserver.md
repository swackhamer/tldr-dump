# minetestserver

> Multiplayer infinite-world block sandbox server. See also: `minetest`, the graphical client. More information: <https://wiki.minetest.org/Setting_up_a_server>.

## Examples

### Start the server

```bash
minetestserver
```

### List available worlds

```bash
minetestserver --world list
```

### Load the specified world

```bash
minetestserver --world world_name
```

### List the available game IDs

```bash
minetestserver --gameid list
```

### Use the specified game

```bash
minetestserver --gameid game_id
```

### Listen on a specific port

```bash
minetestserver --port 34567
```

### Migrate to a different data backend

```bash
minetestserver --migrate sqlite3|leveldb|redis
```

### Start an interactive terminal after starting the server

```bash
minetestserver --terminal
```
