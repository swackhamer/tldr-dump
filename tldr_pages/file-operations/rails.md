# rails

> A server-side MVC framework written in Ruby. Some subcommands such as `generate` have their own usage documentation. More information: <https://guides.rubyonrails.org/command_line.html>.

## Examples

### Create a new rails project

```bash
rails new "project_name"
```

### Generate a scaffold for a model named Post, predefining the attributes title and body

```bash
rails generate scaffold Post title:string body:text
```

### Run migrations

```bash
rails db:migrate
```

### List all routes

```bash
rails routes
```

### Start local server for current project on port 3000

```bash
rails server
```

### Start local server for current project on a specified port

```bash
rails server [-p|--port] "port"
```

### Open console to interact with application from command-line

```bash
rails console
```

### Check current version of rails

```bash
rails [-v|--version]
```
