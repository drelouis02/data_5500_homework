
import requests
import json

url = "https://api.datamuse.com/words?rel_trg=cow"

response = requests.get(url)
word_list = json.loads(response.text)

for item in word_list:
    if item["word"] == "cheese":
        cheese_score = item["score"]
        print("The score for cheese is:", cheese_score)
        break
