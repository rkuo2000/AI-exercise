curl -s http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gemma4:e2b","messages":[{"role":"user","content":"Hi!"}],"max_tokens":256}' \
  | python3 -m json.tool
