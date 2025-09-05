# rails-routes

> List routes in a Rails application. More information: <https://guides.rubyonrails.org/routing.html>.

## Examples

### List all routes

```bash
rails routes
```

### List all routes in an expanded format

```bash
rails routes --expanded
```

### List routes partially matching URL helper method name, HTTP verb, or URL path

```bash
rails routes [-g|--grep] posts_path|GET|/posts
```

### List routes that map to a specified controller

```bash
rails routes [-c|--controller] posts|Posts|Blogs::PostsController
```
