import os
import openai

openai.api_key = "YOUR_KEY_HERE"
completion = openai.Edit.create(
    model="text-davinci-edit-001",
    input="There are three possible traits: power-hungry, lonely, violent.\n\nRYAN\n\nTRAIT: ___\nLIFE GOAL: ____\nVIDEO-GAME STYLE ENEMY NAME: ____\nENEMY ATTACK NAME: ____\nENEMY WEAK TO ATTACK NAMED: ____\nALWAYS CARRY: ____\nFAVOURITE PHRASE: ____\n\n",
    instruction="Fill in the blanks",
    temperature=0.7,
    top_p=1
)

print(completion.choices[0].text.strip())