# clj

> Clojure tool to start a REPL or invoke a function with data. All options can be defined in a `deps.edn` file. More information: <https://clojure.org/guides/deps_and_cli>.

## Examples

### Start a REPL (interactive shell)

```bash
clj
```

### Execute a function

```bash
clj -X namespace/function_name
```

### Run the main function of a specified namespace

```bash
clj -M [-m|--main] namespace args
```

### Prepare a project by resolving dependencies, downloading libraries, and making/caching classpaths

```bash
clj -P
```

### Start an nREPL server with the CIDER middleware

```bash
clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}' [-m|--main] nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive
```

### Start a REPL for ClojureScript and open a web browser

```bash
clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}' [-m|--main] cljs.main [-r|--repl]
```
