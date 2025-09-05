# blackfire

> Monitor, profile and test a PHP application. More information: <https://blackfire.io>.

## Examples

### Initialize and configure the Blackfire client

```bash
blackfire config
```

### Launch the Blackfire agent

```bash
blackfire agent
```

### Launch the Blackfire agent on a specific socket

```bash
blackfire agent --socket="tcp://127.0.0.1:8307"
```

### Run the profiler on a specific program

```bash
blackfire run php path/to/file.php
```

### Run the profiler and collect 10 samples

```bash
blackfire --samples 10 run php path/to/file.php
```

### Run the profiler and output results as JSON

```bash
blackfire --json run php path/to/file.php
```

### Upload a profiler file to the Blackfire web service

```bash
blackfire upload path/to/file
```

### View the status of profiles on the Blackfire web service

```bash
blackfire status
```
