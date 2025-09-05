# sui-client-ptb

> Create, sign and execute programmable transaction blocks. More information: <https://docs.sui.io/references/cli/ptb>.

## Examples

### Call a Move function from a package and module

```bash
sui client ptb --move-call p::m::f "<type>" args
```

### Make a Move vector with two elements of type u64

```bash
sui client ptb --make-move-vec "<u64>" "[1000,2000]"
```

### Split a gas coin and transfer it to address

```bash
sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @address
```

### Transfer an object to an address

```bash
sui client ptb --transfer-objects "[object_id]" @address
```

### Publish a Move package, and transfer the upgrade capability to sender

```bash
sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender
```
