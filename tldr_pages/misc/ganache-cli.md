# ganache-cli

> Command-line version of Ganache, your personal blockchain for Ethereum development. More information: <https://www.trufflesuite.com/ganache>.

## Examples

### Run Ganache

```bash
ganache-cli
```

### Run Ganache with a specific number of accounts

```bash
ganache-cli --accounts=number_of_accounts
```

### Run Ganache and lock available accounts by default

```bash
ganache-cli --secure
```

### Run Ganache server and unlock specific accounts

```bash
ganache-cli --secure --unlock "account_private_key1" --unlock "account_private_key2"
```

### Run Ganache with a specific account and balance

```bash
ganache-cli --account="account_private_key,account_balance"
```

### Run Ganache with accounts with a default balance

```bash
ganache-cli --defaultBalanceEther=default_balance
```

### Run Ganache and log all requests to `stdout`

```bash
ganache-cli --verbose
```
