# cmctl

> Manage cert-manager resources inside your cluster. Check cert signing status, approve/deny requests, and issue new certificate requests. More information: <https://cert-manager.io/docs/usage/cmctl/>.

## Examples

### Check if the cert-manager API is ready

```bash
cmctl check api
```

### Check the status of a certificate

```bash
cmctl status certificate cert_name
```

### Create a new certificate request based on an existing certificate

```bash
cmctl create certificaterequest my-cr --from-certificate-file cert.yaml
```

### Create a new certificate request, fetch the signed certificate, and set a maximum wait time

```bash
cmctl create certificaterequest my-cr --from-certificate-file cert.yaml --fetch-certificate --timeout 20m
```
