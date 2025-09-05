# hsd-cli

> The REST tool for the Handshake blockchain. More information: <https://handshake.org>.

## Examples

### Retrieve information about the current server

```bash
hsd-cli info
```

### Broadcast a local transaction

```bash
hsd-cli broadcast transaction_hex
```

### Retrieve a mempool snapshot

```bash
hsd-cli mempool
```

### View a transaction by address or hash

```bash
hsd-cli tx address_or_hash
```

### View a coin by its hash index or address

```bash
hsd-cli coin hash_index_or_address
```

### View a block by height or hash

```bash
hsd-cli block height_or_hash
```

### Reset the chain to the specified block

```bash
hsd-cli reset height_or_hash
```

### Execute an RPC command

```bash
hsd-cli rpc command args
```
