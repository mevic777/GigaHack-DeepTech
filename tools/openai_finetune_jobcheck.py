# Made by Deliu Marius
# Team 1D3M

import openai
import json
import time

openai.api_key = open("openai_key", "r").read()

job = input("Job ID: ")

while True:
    print(openai.FineTuningJob.retrieve(job))
    print("-----------------------------------------------------------")
    print(json.loads(str(openai.FineTuningJob.list_events(id=job, limit=10)))['data'][0])
    time.sleep(60)