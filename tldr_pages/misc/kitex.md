# kitex

> Code generation tool provided by the Go RPC framework Kitex. Kitex accepts both thrift and protobuf IDLs, and supports generating a skeleton of a server side project. More information: <https://www.cloudwego.io>.

## Examples

### Generate client codes when a project is in `$GOPATH`

```bash
kitex path/to/IDL_file.thrift
```

### Generate client codes when a project is not in `$GOPATH`

```bash
kitex -module github.com/xx-org/xx-name path/to/IDL_file.thrift
```

### Generate client codes with protobuf IDL

```bash
kitex -type protobuf path/to/IDL_file.proto
```

### Generate server codes

```bash
kitex -service svc_name path/to/IDL_file.thrift
```
