# pio-remote

> Helper command for PlatformIO Remote Development. `pio remote [command]` takes the same arguments as its locally executing counterpart `pio [command]`. More information: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

## Examples

### List all active Remote Agents

```bash
pio remote agent list
```

### Start a new Remote Agent with a specific name and share it with friends

```bash
pio remote agent start [-n|--name] agent_name [-s|--share] example1@example.com [-s|--share] example2@example.com
```

### List devices from specified Agents (omit `--agent` to specify all Agents)

```bash
pio remote --agent agent_name1 --agent agent_name2 device list
```

### Connect to the serial port of a remote device

```bash
pio remote --agent agent_name device monitor
```

### Run all targets on a specified Agent

```bash
pio remote --agent agent_name run
```

### Update installed core packages, development platforms and global libraries on a specific Agent

```bash
pio remote --agent agent_name update
```

### Run all tests in all environments on a specific Agent

```bash
pio remote --agent agent_name test
```
