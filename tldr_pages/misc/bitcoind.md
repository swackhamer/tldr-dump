# bitcoind

> Bitcoin Core daemon. Uses the configuration defined in `bitcoin.conf`. More information: <https://manned.org/bitcoind>.

## Examples

### Start the Bitcoin Core daemon (in the foreground)

```bash
bitcoind
```

### Start the Bitcoin Core daemon in the background (use `bitcoin-cli stop` to stop)

```bash
bitcoind -daemon
```

### Start the Bitcoin Core daemon on a specific network

```bash
bitcoind -chain=main|test|signet|regtest
```

### Start the Bitcoin Core daemon using specific configuration file and data directory

```bash
bitcoind -conf=path/to/bitcoin.conf -datadir=path/to/directory
```
