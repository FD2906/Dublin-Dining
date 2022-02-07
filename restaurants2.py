import json 

with open('dataset.json') as dataset_json:
    dataset = json.load(dataset_json)
    
print(dataset)

