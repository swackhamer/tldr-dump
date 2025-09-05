# twurl

> Curl-like command but tailored specifically for the Twitter API. More information: <https://github.com/twitter/twurl>.

## Examples

### Authorize `twurl` to access a Twitter account

```bash
twurl authorize [-c|--consumer-key] twitter_api_key [-s|--consumer-secret] twitter_api_secret
```

### Make a GET request to an API endpoint

```bash
twurl [-X|--request-method] GET twitter_api_endpoint
```

### Make a POST request to an API endpoint

```bash
twurl [-X|--request-method] POST [-d|--data] 'endpoint_params' twitter_api_endpoint
```

### Upload media to Twitter

```bash
twurl [-H|--host] "twitter_upload_url" [-X|--request-method] POST "twitter_upload_endpoint" [-f|--file] "path/to/media.jpg" [-F|--file-field] "media"
```

### Access a different Twitter API host

```bash
twurl [-H|--host] twitter_api_url [-X|--request-method] GET twitter_api_endpoint
```

### Create an alias for a requested resource

```bash
twurl alias alias_name resource
```
