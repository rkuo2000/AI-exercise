## Ollama之使用

### 安裝 Ollama
`curl -fsSL https://ollama.com/install.sh | sh` <br>

#### 下載模型與執行
`ollama run gemma4:e4b --verbose`<br>

#### 模型參數修改
編輯 Modelfile 文字檔 (內容如下)
```
FROM gemma4:e4b
PARAMETER num_ctx 131072
```

#### 設定參數與產生模型檔
`ollama create gemma4-128K:e2b -f Modelfile` <br>

#### 列出模型
`ollama list` <br>

#### 查看process
`ollama ps` <br>
```
NAME          ID              SIZE      PROCESSOR    CONTEXT    UNTIL             
gemma4:e2b    7fbdbf8f5e45    1.9 GB    100% GPU     32768      4 minutes from now
```

#### 停止proces
`ollama stop gemma4:e2b`<br>

#### 移除模型
`ollama rm gemma4:e2b` <br>
