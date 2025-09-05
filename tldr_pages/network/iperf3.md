# iperf3

> Traffic generator for testing network bandwidth. More information: <https://iperf.fr>.

## Examples

### Run iperf3 as a server

```bash
iperf3 [-s|--server]
```

### Run an iperf3 server on a specific port

```bash
iperf3 [-s|--server] [-p|--port] port
```

### Start bandwidth test

```bash
iperf3 [-c|--client] server
```

### Run iperf3 in multiple parallel streams

```bash
iperf3 [-c|--client] server [-P|--parallel] streams
```

### Reverse direction of the test. Server sends data to the client

```bash
iperf3 [-c|--client] server [-R|--reverse]
```
