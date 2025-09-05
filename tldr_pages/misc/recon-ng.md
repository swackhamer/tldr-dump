# recon-ng

> Automated reconnaissance and information gathering tool. More information: <https://github.com/lanmaster53/recon-ng/wiki>.

## Examples

### Start the tool

```bash
recon-ng
```

### Create a workspace

```bash
workspaces create workspace_name
```

### Search the marketplace for modules used to accomplish different reconnaissance tasks

```bash
marketplace search
```

### Install all available modules (some may need API keys to function completely)

```bash
marketplace install all
```

### Load the profiler module. It is used to scan the web for profiles matching the target, scrape them, and store them

```bash
modules load profiler
```

### Insert the target's username. After entering this command, enter the desired username of the search and leave the rest of the options blank

```bash
db insert profiles
```

### Run the current module

```bash
run
```
