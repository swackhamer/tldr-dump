# hsw-cli

> The REST tool for the Handshake wallet. More information: <https://github.com/handshake-org/hs-client>.

## Examples

### Unlock the current wallet (timeout in seconds)

```bash
hsw-cli unlock passphrase timeout
```

### Lock the current wallet

```bash
hsw-cli lock
```

### View the current wallet's details

```bash
hsw-cli get
```

### View the current wallet's balance

```bash
hsw-cli balance
```

### View the current wallet's transaction history

```bash
hsw-cli history
```

### Send a transaction with the specified coin amount to an address

```bash
hsw-cli send address 1.05
```

### View the current wallet's pending transactions

```bash
hsw-cli pending
```

### View details about a transaction

```bash
hsw-cli tx transaction_hash
```
