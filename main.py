import ollama

while True:
	user_console_input = input("Write something: ") # writes output to console

	prompt_to_llama = """
		System: You are a helpful command line assistant. Provide only the exact command(s) needed, without any explanation or additional text. Do not use markdown formatting. 
		User input: {}
	""".format(user_console_input)

	stream = ollama.chat(
		model='llama3.2',
		messages=[{'role': 'user', 'content': prompt_to_llama}],
		stream=True,
	)
	
	for chunk in stream:
		print(chunk['message']['content'], end='', flush=True)
	
	# Add some separation to the console output
	print()
	print()
	print()




exit() ########### REMOVE AFTER USE ###########

