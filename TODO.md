Final goal: Build a pentesting tool that you can chat and it just runs commands for you.
IMPORTANT: execute as root as your own responsability, it's required for many nmap scans.

TO DO:
[x] Find a way to translate words into commands (I suppose using Llama).
[x] Find a way to execute those commands.
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
[x] Find a way to make the program interactive (input from console).
[x] Find a way to get just the nmap command.
	- Study how to write a good prompt on llama
[x] Find a way to execute those commands.
	- Pending: improve it.
[x] Download dictionaries https://github.com/danielmiessler/SecLists.git to use with gobuster generated-commands

----------------------


Key points:
	- How to get control before the command is executed? if? retry?
	- How to put constraints that needs to be completed before any command? -> custom inputs by hand? for example domain, etc. How to handle errors?
	- Use of selenium to browser-related tasks?
	- How to feed llama with useful links like SecLists for fuzzing? Or links with cheatsheets of hacking, etc. MindsDB?
	- Separate with stages with custom menu? Like Discovery stage, exploitation, etc
	- I feel that i have to give to llama a lot of knoledge on how to hack, which stuff be careful, etc, improve prompts, include context (domain, constraints, sites, etc).

Usage:
	- Say to llama that we want to conduct a pentest on this domain, using this techniches, with this restrictions


----------------------


# IMPORTANT KEY NOTES:
#       - You have to teach to llama how to hack (guide like a kid)
#       - Simplify the process to 1 o 2 attacks (maybe fuzzing for domain discovery, etc)
#       - You can use llama to get commands (already) and also to interpret the results (after i teach like a kid), also you can use llama to make checks for the command and ask for a thing and exit the program. Give feedback and exit. To not implement everyhing. Not run until all the criteria is completed.
#       - You can rely on llama to anything you want. Is up to you how much you program and how much you give to llama
#       - You can use also Selenium to open the browser o whatever, you can do whatever you want. Its a python program.
