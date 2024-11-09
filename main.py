import ollama

response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Just give me the command of nmap to scan ports from 1 to 1000 using TCP SYN ',
  },
])

print(response['message']['content'])
