import ollama
import os
import subprocess

# How this program works?
# 1. [DONE] Convert natural language to hacking command (nmap or gobuster for now)
# 2. Checks before executing
# 3. Execute command
# 4. Output results in a simple and short way (LLM again)


# Mandatory fields
domain = input("Domain or IP to attack: ")
if not domain:
	print("You must provide a valid domain or IP address to continue.")
	exit()

# Dictionaries for gobuster
if not os.path.exists("./SecLists"):
	print("You must download https://github.com/danielmiessler/SecLists.git")
	exit()


# call llama
def llama(prompt):
	response = ollama.chat(model='llama3.2', messages=[
		{
			'role': 'user',
			'content': prompt,
		},
	])
	llama_response = response['message']['content']
	print(llama_response)
	return llama_response


# Get hacking command based on natural language
def get_hacking_command(user_console_input):
	# Prompt to get only commands based on user input. We also teach how llama must respond on specific scenarios.
	prompt_to_llama = """
		System: You are a command line assistant. You guess commands based on natural language. Provide only the exact command needed, without any explanation or additional text. Do not use markdown formatting.
		System: You must respond ONLY with one command and its arguments based on common examples: could be nmap or gobuster. Not any other command.
		
		User input: {}
        User input: {}
	""".format(domain, user_console_input)

	print("Loading...")
	# Send prompt to llama
	hacking_command = llama(prompt_to_llama)
	
	return hacking_command # return hacking command


# Get relative path local dictionary based on a guessed dictionary
def find_dictionary_local(dictionary_guessed):
	for root, dirs, files in os.walk("./SecLists"):
		for file in files:
			if dictionary_guessed in file:
				local_dictionary = os.path.relpath(os.path.join(root, file), start="./SecLists")
				print("Found local dictionary at: ",local_dictionary)
				return local_dictionary



# Main loop
while True:
	# User input from console
	user_console_input = input("Describe attack: ") # writes output to console

	hacking_command = get_hacking_command(user_console_input)

	# check if is gobuster to include dictionaries paths in the prompt
	if "gobuster" in hacking_command:
		print("gobuster command detected!")

		# PROGRAMAR EL DICTIONARY GUESSER. FALLA MUCHO. Solamente hacer un in en todos los directiios y listo
		print("Guessing dictionary to apply... (it takes a while, please be patient!)")
		dictionary_guessed = llama("You are a dictionary guesser based on the following user request: {}. You must respond with just 1 file name from https://github.com/danielmiessler/SecLists. Provide only the exact file name needed, without any explanation or additional text. Remove everything except the filename and its extension. Just the txt file name with its extension. Do not use markdown formatting.".format(user_console_input))
		print("Dictionary guessed: ", dictionary_guessed)
		
		print("Finding dictionary locally...")

		# System: The additional info for gobuster are all the possible files that llama can select in order to do a brute-force attack using gobuster. Just select 1 file path and use it in the gobuster command.
		# System: Please note that you must replace the path to wordlist with the actual path to your guessed wordlist file, and ensure that it's in a format compatible with Gobuster.
		# System: Additional info for gobuster: {}
		# from this variable seclists_file_names

		local_dictionary = find_dictionary_local(dictionary_guessed)

		exit()
	
	# if not, is a nmap
	print("nmap command detected!")

	# Use hacking_command to execute command
	print("COMMAND EXECUTION: " + hacking_command)
	
	try:
		output = subprocess.check_output([hacking_command], shell=True)
		print(output)
	except subprocess.CalledProcessError as e:
		print(f"Command failed with error: {e}")
		print("Try again!")
		continue
