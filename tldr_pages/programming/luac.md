# luac

> Lua bytecode compiler. More information: <https://www.lua.org/manual/5.4/luac.html>.

## Examples

### Compile a Lua source file to Lua bytecode

```bash
luac -o byte_code.luac source.lua
```

### Do not include debug symbols in the output

```bash
luac -s -o byte_code.luac source.lua
```
