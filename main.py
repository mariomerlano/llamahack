import ollama
import os
import subprocess

# Mandatory fields
domain = input("Domain or IP to attack: ")
if not domain:
	print("You must provide a valid domain or IP address to continue.")
	exit()

# Dictionaries for gobuster
if not os.path.exists("./SecLists"):
	print("You must download https://github.com/danielmiessler/SecLists.git")
	exit()

# Create a variable with all the files from SecLists
seclists_file_names = ""
for root, dirs, files in os.walk("./SecLists"):
	for file in files:
		# print(os.path.join(root, file))
		seclists_file_names += os.path.join(root, file) + "\n"
# print(seclists_file_names)

while True:
	# User input from console
	user_console_input = input("Describe attack: ") # writes output to console

	# Prompt to get only commands based on user input. We also teach how llama must respond on specific scenarios.
	prompt_to_llama = """
		System: You are a helpful command line assistant. Provide only the exact command(s) needed, without any explanation or additional text. Do not use markdown formatting. You can also respond only when some argument given by the user is missing.
        System: For now, you must be limited just to 2 commands: nmap and gobuster with their specific flags and arguments.
	System: Additional info for gobuster: {}
	System: The additional info for gobuster are all the possible files that llama can select in order to do a brute-force attack using gobuster. Just select 1 file path and use it in the gobuster command.
	System: Please note that you must replace the path to wordlist with the actual path to your guessed wordlist file, and ensure that it's in a format compatible with Gobuster.
		User input: {}
        	User input: {}
        System: You must only output 1 command.
	""".format(seclists_file_names, domain, user_console_input)

	# Send prompt to llama
	stream = ollama.chat(
		model='llama3.2',
		messages=[{'role': 'user', 'content': prompt_to_llama}],
		stream=True,
	)
	
	# Return response word by word in the terminal and store it on response_command
	response_command = ""
	for chunk in stream:
		print(chunk['message']['content'], end='', flush=True)
		response_command += chunk['message']['content']
	
	# Add some separation to the console output
	print()
	print()
	print()

	# Use response_command to execute command
	print("COMMAND EXECUTION: " + response_command)
	output = subprocess.check_output([response_command], shell=True)



exit() ########### REMOVE AFTER USE ###########

