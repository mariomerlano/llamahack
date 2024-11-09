import ollama

while True:
	# User input from console
	user_console_input = input("Write something: ") # writes output to console

	# Prompt to get only commands based on user input
	prompt_to_llama = """
		System: You are a helpful command line assistant. Provide only the exact command(s) needed, without any explanation or additional text. Do not use markdown formatting. 
		User input: {}
	""".format(user_console_input)

	# Send prompt to llama
	stream = ollama.chat(
		model='llama3.2',
		messages=[{'role': 'user', 'content': prompt_to_llama}],
		stream=True,
	)
	
	# Read llama output word by word
	for chunk in stream:
		print(chunk['message']['content'], end='', flush=True)
	
	# Add some separation to the console output
	print()
	print()
	print()




exit() ########### REMOVE AFTER USE ###########

