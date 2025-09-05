# bing-rewards

> Automate daily Bing Rewards points. More information: <https://github.com/jack-mil/bing-rewards>.

## Examples

### Complete both desktop and mobile searches

```bash
bing-rewards
```

### Run 10 searches with mobile user-agent

```bash
bing-rewards [-m|--mobile] [-c|--count] 10
```

### Complete mobile and desktop searches using specified Chrome profile "Profile 1"

```bash
bing-rewards --profile "Profile 1"
```

### Run searches sequentially across multiple Chrome profiles

```bash
bing-rewards --profile "Default" "Profile 1" "Profile 2"
```

### Display help

```bash
bing-rewards [-h|--help]
```
