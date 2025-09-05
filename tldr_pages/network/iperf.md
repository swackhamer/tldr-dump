# iperf

> Measure network bandwidth between computers. More information: <https://iperf.fr>.

## Examples

### Run on server

```bash
iperf [-s|--server]
```

### Run on server using UDP mode and set server port to listen on 5001

```bash
iperf [-u|--udp] [-s|--server] [-p|--port] 5001
```

### Run on client

```bash
iperf [-c|--client] server_address
```

### Run on client every 2 seconds

```bash
iperf [-c|--client] server_address [-i|--interval] 2
```

### Run on client with 5 parallel threads

```bash
iperf [-c|--client] server_address [-P|--parallel] 5
```

### Run on client using UDP mode

```bash
iperf [-u|--udp] [-c|--client] server_address [-p|--port] 5001
```
