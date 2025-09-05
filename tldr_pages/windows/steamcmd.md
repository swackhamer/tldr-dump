# steamcmd

> A command-line version of the Steam client. More information: <https://manned.org/steamcmd>.

## Examples

### Install or update an application anonymously

```bash
steamcmd +login anonymous +app_update appid +quit
```

### Install or update an application using the specified credentials

```bash
steamcmd +login username +app_update appid +quit
```

### Install an application for a specific platform

```bash
steamcmd +@sSteamCmdForcePlatformType windows +login anonymous +app_update appid validate +quit
```

### Clear cached login credentials for a user

```bash
steamcmd +login username +logout +quit
```
