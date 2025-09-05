# gcloud-auth

> Grant and revoke authorization to `gcloud` and manage credentials. See also: `gcloud`. More information: <https://cloud.google.com/sdk/gcloud/reference/auth>.

## Examples

### Authorize Google Cloud access for the `gcloud` CLI with Google Cloud user credentials and set the current account as active

```bash
gcloud auth login
```

### Authorize Google Cloud access similar to `gcloud auth login` but with service account credentials

```bash
gcloud auth activate-service-account
```

### Manage Application Default Credentials (ADC) for Cloud Client Libraries

```bash
gcloud auth application-default
```

### Display a list of Google Cloud accounts currently authenticated on your system

```bash
gcloud auth list
```

### Display the current account's access token

```bash
gcloud auth print-access-token
```

### Remove access credentials for an account

```bash
gcloud auth revoke
```
