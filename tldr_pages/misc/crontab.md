# crontab

> Schedule cron jobs to run on a time interval for the current user. More information: <https://manned.org/crontab>.

## Examples

### Edit the crontab file for the current user

```bash
crontab -e
```

### Edit the crontab file for a specific user

```bash
sudo crontab -e -u user
```

### Replace the current crontab with the contents of the given file

```bash
crontab path/to/file
```

### View a list of existing cron jobs for current user

```bash
crontab -l
```

### Remove all cron jobs for the current user

```bash
crontab -r
```

### Sample job which runs at 10:00 every day (* means any value)

```bash
0 10 * * * command_to_execute
```

### Sample crontab entry, which runs a command every 10 minutes

```bash
*/10 * * * * command_to_execute
```

### Sample crontab entry, which runs a certain script at 02:30 every Friday

```bash
30 2 * * Fri /path/to/script.sh
```
