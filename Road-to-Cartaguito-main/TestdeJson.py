import json

import os

filename = "SaveFile.json"
with open(filename, "r") as f:
    data = json.load(f)
print(data['players'][0])
for x in data['players']:
    print(x['User'])
    
    
