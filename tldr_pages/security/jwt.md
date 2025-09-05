# jwt

> Work with JSON Web Tokens (JWTs). Encryption algorithms available are HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384. More information: <https://github.com/mike-engel/jwt-cli>.

## Examples

### Decode a JWT

```bash
jwt decode jwt_string
```

### Decode a JWT as a JSON string

```bash
jwt decode [-j|--json] jwt_string
```

### Encode a JSON string to a JWT

```bash
jwt encode [-A|--alg] HS256 [-S|--secret] 1234567890 'json_string'
```

### Encode key pair payload to JWT

```bash
jwt encode [-A|--alg] HS256 [-S|--secret] 1234567890 [-P|--payload] key=value
```
