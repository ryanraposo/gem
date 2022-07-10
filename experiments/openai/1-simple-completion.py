# Simple OpenAI completion playground

import os
import openai


def getCompletion(prompt):
    openai.api_key = os.environ.get("OPENAI_API_KEY") 
    completion = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1028
    )
    return completion.choices[0].text.strip()

while True:
    input_prompt = input("Enter a prompt:")
    completion = getCompletion(input_prompt)
    print(completion)
