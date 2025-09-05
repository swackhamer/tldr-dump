# pm2

> Process manager for Node.js. Used for log management, monitoring and configuring processes. More information: <https://pm2.keymetrics.io>.

## Examples

### Start a process with a name that can be used for later operations

```bash
pm2 start app.js --name application_name
```

### List processes

```bash
pm2 list
```

### Monitor all processes

```bash
pm2 monit
```

### Stop a process

```bash
pm2 stop application_name
```

### Restart a process

```bash
pm2 restart application_name
```

### Dump all processes for resurrecting them later

```bash
pm2 save
```

### Resurrect previously dumped processes

```bash
pm2 resurrect
```
