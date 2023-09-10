# Made by Deliu Marius
# Team 1D3M

import openai
import json
import time

# TODO
# - solve the pending time problem for uploaded files - catch exception?

openai.api_key = open("openai_key", "r").read()

# The file to be sent to finetuning is usually the last one
# in the JSON filelist, which we request through an API call

filename = "ft-003"

print('[+] Sending file to OpenAI...')
openai.File.create(
  file=open("finetuned_data.jsonl", "rb"),
  purpose='fine-tune',
  user_provided_filename=filename
)
print('[v] Done!')

# Requesting filelist
print('[+] Requesting filelist...')
filelist = json.loads(str(openai.File.list()))
print('[v] Received!')

#jobid = 'file-NyL0a696jH5NqS1ii2EOacGd'
jobid = ''

print('[+] Processing...')
# Sometimes, it takes a while for the site to
# process uploaded files
time.sleep(300)

# Iterating through filelist and finding the id of the just-uploaded file
print('[+] Finding jobid...')
for obj in filelist['data']:
    if obj['filename'] == filename:
        jobid = obj['id']
        break

# Sending the file to finetuning
print('[+] Staring finetuning job...')
job = json.loads(str(openai.FineTuningJob.create(training_file=jobid, model="gpt-3.5-turbo-0613", suffix="docky-03-research")))
print(job)
print('[+] Job started!')
print('[+] Jobid: ' + job['id'])