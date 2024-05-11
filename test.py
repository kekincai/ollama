import ollama
response = ollama.chat(model='llama3:8b', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])
