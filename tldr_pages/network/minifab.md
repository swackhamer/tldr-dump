# minifab

> Automate the setup and deployment of Hyperledger Fabric networks. More information: <https://github.com/hyperledger-labs/minifabric>.

## Examples

### Bring up the default Hyperledger Fabric network

```bash
minifab up [-i|--fabric-release] minifab_version
```

### Bring down the Hyperledger Fabric network

```bash
minifab down
```

### Install chaincode onto a specified channel

```bash
minifab install [-n|--chaincode-name] chaincode_name
```

### Install a specific chaincode version onto a channel

```bash
minifab install [-n|--chaincode-name] chaincode_name [-v|--chaincode-version] chaincode_version
```

### Initialize the chaincode after installation/upgrade

```bash
minifab approve,commit,initialize,discover
```

### Invoke a chaincode method with the specified arguments

```bash
minifab invoke [-n|--chaincode-name] chaincode_name [-p|--chaincode-parameters] '"method_name", "argument1", "argument2", ...'
```

### Make a query on the ledger

```bash
minifab blockquery block_number
```

### Quickly run an application

```bash
minifab apprun [-l|--chaincode-language] app_programming_language
```
