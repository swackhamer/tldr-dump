# cosign

> Container Signing, Verification and Storage in an OCI registry. More information: <https://github.com/sigstore/cosign>.

## Examples

### Generate a key-pair

```bash
cosign generate-key-pair
```

### Sign a container and store the signature in the registry

```bash
cosign sign -key cosign.key image
```

### Sign a container image with a key pair stored in a Kubernetes secret

```bash
cosign sign -key k8s://namespace/key image
```

### Sign a blob with a local key pair file

```bash
cosign sign-blob --key cosign.key path/to/file
```

### Verify a container against a public key

```bash
cosign verify -key cosign.pub image
```

### Verify images with a public key in a Dockerfile

```bash
cosign dockerfile verify -key cosign.pub path/to/Dockerfile
```

### Verify an image with a public key stored in a Kubernetes secret

```bash
cosign verify -key k8s://namespace/key image
```

### Copy a container image and its signatures

```bash
cosign copy example.com/src:latest example.com/dest:latest
```
