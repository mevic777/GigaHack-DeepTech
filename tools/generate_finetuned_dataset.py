import json

raw_data = open("biomedical_research_dataset.json", "r").read()
finetuned_data = open("finetuned_data.jsonl", "w")

# Here, we define the personality of the language model by verbosely dictating his occupation and traits
personality = open("personality", "r").read()

# Some undesirable characters which mess up the file
antichars = [ '\n', '\r', '\t', '"' ]

# Formatting raw data as JSON
raw_data_json = json.loads(raw_data)

for q in raw_data_json["questions"]:
    body = str(q["body"])
    # Cleaning text from unwanted characters
    for c in antichars:
        body = body.replace(c, '')
    answer = q["ideal_answer"]

    # Some questions have more than one ideal_answer, so we account for all of them
    for a in answer:
        a = str(a)
        # Cleaning text from unwanted characters
        for c in antichars:
            a = a.replace(c, '')
        finetuned_data.write('{"messages":[{"role":"system", "content":' + f'"{personality}"' + '}, {"role":"user", "content":' + f'"{body}"' + '}, {"role":"assistant","content":' + f'"{a}"' + '}]}\n')