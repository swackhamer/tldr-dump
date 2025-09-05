# ibmcloud-login

> Log in to the IBM Cloud. More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

## Examples

### Log in by using an interactive prompt

```bash
ibmcloud login
```

### Log in to a specific API endpoint (default is `cloud.ibm.com`)

```bash
ibmcloud login -a api_endpoint
```

### Log in by providing username, password and the targeted region as parameters

```bash
ibmcloud login -u username -p password -r us-south
```

### Log in with an API key, passing it as an argument

```bash
ibmcloud login --apikey api_key_string
```

### Log in with an API key, passing it as a file

```bash
ibmcloud login --apikey @path/to/api_key_file
```

### Log in with a federated ID (single sign-on)

```bash
ibmcloud login --sso
```
