# swagger-codegen

> Generate code and documentation for your REST api from a OpenAPI/swagger definition. More information: <https://github.com/swagger-api/swagger-codegen>.

## Examples

### Generate documentation and code from an OpenAPI/swagger file

```bash
swagger-codegen generate [-i|--input-spec] swagger_file [-l|--lang] language
```

### Generate Java code using the library retrofit2 and the option useRxJava2

```bash
swagger-codegen generate [-i|--input-spec] http://petstore.swagger.io/v2/swagger.json [-l|--lang] java --library retrofit2 -DuseRxJava2=true
```

### List available languages

```bash
swagger-codegen langs
```

### Display help for a specific command

```bash
swagger-codegen generate|config-help|meta|langs|version --help
```
