Final goal: Build a pentesting tool that you can chat and it just runs commands for you.

TO DO:
[ ] Find a way to translate words into commands (I suppose using Llama).
[ ] Find a way to execute those commands.
[ ] Find a way to output useful insights.

Evaluate stack:
[x] Ollama, the easiest way to start (https://ollama.com/)
	- Download from https://ollama.com/download
	- ollama run llama3.2 (run local model)
[ ] Llama 3.1? -> LLM optimized for NLP tasks
[ ] Llama 3.2? -> LLM text and images
[ ] LlamaIndex? -> ??
[ ] Evaluate https://github.com/mindsdb/mindsdb for storing and processing data

Building process:
[x] How to call Ollama from Python?
	- https://github.com/ollama/ollama-python
	- pip install ollama
	- API Docs: https://github.com/ollama/ollama/blob/main/docs/api.md
[x] Test Llama3.2
	- Translate words into nmap commands successfully, but theres so much explanation. 
[x] Changed mode from chat to streaming (better experience) [stream=True flag].
[ ] Find a way to make the program interactive (input from console).
[ ] Find a way to get just the nmap command.
