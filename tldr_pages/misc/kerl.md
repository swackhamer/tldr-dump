# kerl

> Build and install Erlang/OTP instances with ease. More information: <https://github.com/kerl/kerl>.

## Examples

### Build and install an Erlang/OTP version in a directory

```bash
kerl build-install 28.0 28.0 path/to/installation_directory/28.0
```

### Activate an Erlang/OTP installation

```bash
. path/to/installation/activate
```

### Deactivate the current Erlang/OTP installation

```bash
kerl_deactivate
```

### List all available Erlang/OTP releases

```bash
kerl list releases
```

### List installed Erlang/OTP builds

```bash
kerl list installations
```
