# bitcoin-cli

> Client to interact with the Bitcoin Core daemon via RPC calls. Uses the configuration defined in `bitcoin.conf`. More information: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

## Examples

### Send a transaction to a given address

```bash
bitcoin-cli sendtoaddress "address" amount
```

### Generate one or more blocks

```bash
bitcoin-cli generate num_blocks
```

### Print high-level information about the wallet

```bash
bitcoin-cli getwalletinfo
```

### List all outputs from previous transactions available to fund outgoing transactions

```bash
bitcoin-cli listunspent
```

### Export the wallet information to a text file

```bash
bitcoin-cli dumpwallet "path/to/file"
```

### Get blockchain information

```bash
bitcoin-cli getblockchaininfo
```

### Get network information

```bash
bitcoin-cli getnetworkinfo
```

### Stop the Bitcoin Core daemon

```bash
bitcoin-cli stop
```
