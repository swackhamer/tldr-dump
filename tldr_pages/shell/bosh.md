# bosh

> Deploy and manage the BOSH director. More information: <https://bosh.io/docs/cli-v2/>.

## Examples

### Create local alias for director in a specific environment

```bash
bosh alias-env environment_name [-e|--environment] ip_address|URL --ca-cert ca_certificate
```

### List environments

```bash
bosh environments
```

### Log in to the director

```bash
bosh login [-e|--environment] environment
```

### List deployments

```bash
bosh [-e|--environment] environment deployments
```

### List environment virtual machines in a deployment

```bash
bosh [-e|--environment] environment vms [-d|--deployment] deployment
```

### SSH into virtual machine

```bash
bosh [-e|--environment] environment ssh virtual_machine [-d|--deployment] deployment
```

### Upload stemcell

```bash
bosh [-e|--environment] environment upload-stemcell stemcell_file|url
```

### Show current cloud config

```bash
bosh [-e|--environment] environment cloud-config
```
