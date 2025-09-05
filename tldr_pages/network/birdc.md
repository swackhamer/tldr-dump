# birdc

> BIRD remote control. Retrieve information like routes from bird and perform configurations during runtime. More information: <https://bird.network.cz/?get_doc&v=30&f=bird-4.html>.

## Examples

### Open the remote control console

```bash
birdc
```

### Reload the configuration without restarting BIRD

```bash
birdc configure
```

### Show the current status of BIRD

```bash
birdc show status
```

### Show all configured protocols

```bash
birdc show protocols
```

### Show all details about a protocol

```bash
birdc show protocols upstream1 all
```

### Show all routes that contain a specific AS number

```bash
birdc "show route where bgp_path ~ [4242120045]"
```

### Show all best routes

```bash
birdc show route primary
```

### Show all details of all routes from a given prefix

```bash
birdc show route for fd00:/8 all
```
