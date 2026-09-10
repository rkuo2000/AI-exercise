## [Ollama](https://github.com/ollama/ollama)

### Install
`curl -fsSL https://ollama.com/install.sh | sh` <br>

---
### Flags
`ollama -h` (help)<br>

`ollama -v` (version)<br>

---
### Command
ollama [command]: <br>
```
  serve        Start Ollama
  create       Create a model
  show         Show information for a model
  run          Run a model
  stop         Stop a running model
  pull         Pull a model from a registry
  push         Push a model to a registry
  signin       Sign in to ollama.com
  signout      Sign out from ollama.com
  list         List models
  ps           List running models
  cp           Copy a model
  rm           Remove a model
  launch       Launch the Ollama menu or an integration
  help         Help about any command
```

---
### Ex.
* download a model : `ollama pull gemma4:e4b`
* list models : `ollama list`
* remove a model : `ollama rm gemma4:e4b`
* run a model : `ollama run gemma4:e4b --verbose`
* list running model : `ollama ps`
```
NAME          ID              SIZE      PROCESSOR    CONTEXT    UNTIL              
gemma4:e4b    7fbdbf8f5e45    1.9 GB    100% GPU     32768      4 minutes from now 
```
* stop running model : `ollama stop gemma4:e4b` <br>

#### Launch IDEs
`ollama launch opencode --model gemma4:e4b` <br>
`ollama launch claude` <br>
`ollama launch hermes` <br>

---
### Create Model

#### adjust Context-Size
edit Modelfile <br>
```
FROM gemma4:e4b
PARAMETER num_ctx 131072
```

#### create a model
`ollama create gemma4-128K:e4b -f Modelfile`<br>

#### run a model
`ollama run gemm4-128k:e4b --verbose`<br>
