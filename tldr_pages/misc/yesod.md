# yesod

> Helper tool for Yesod, a Haskell-based web framework. All Yesod commands are invoked through the `stack` project manager. More information: <https://github.com/yesodweb/yesod>.

## Examples

### Create a new scaffolded site, with SQLite as backend, in the `my-project` directory

```bash
stack new my-project yesod-sqlite
```

### Install the Yesod CLI tool within a Yesod scaffolded site

```bash
stack build yesod-bin cabal-install --install-ghc
```

### Start development server

```bash
stack exec -- yesod devel
```

### Touch files with altered Template Haskell dependencies

```bash
stack exec -- yesod touch
```

### Deploy application using Keter (Yesod's deployment manager)

```bash
stack exec -- yesod keter
```
