# Made by Deliu Marius
# Team 1D3M

import openai

# TODO:
# - find a safer alternative to give the program the API key

# Fixating personality
personality = open("personality", "r").read()

# Setting api key
openai.api_key = open("openai_key", "r").read()

# Requesting prompt from user
prompt = input("ChatGPT prompt: ")

# Sending prompt to OpenAI
completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:wisecube-ai:docky-01:7x6peZW6",
        messages=[
            { "role": "system", "content":f'"{personality}"'},
            { "role": "user", "content": prompt}
            ]
        )

# Printing answer given
print(completion.choices[0].message)
