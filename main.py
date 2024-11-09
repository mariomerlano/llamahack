import ollama

while True:
	user_console_input = input("Write something: ") # writes output to console

	stream = ollama.chat(
		model='llama3.2',
		messages=[{'role': 'user', 'content': user_console_input}],
		stream=True,
	)
	
	for chunk in stream:
		print(chunk['message']['content'], end='', flush=True)
	
	# Add some separation to the console output
	print()
	print()
	print()




exit() ########### REMOVE AFTER USE ###########

