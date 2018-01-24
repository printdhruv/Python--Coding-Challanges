""" 
#  Programmer     : Dhruv Patel
#  Problem Name   : Level_2 JSON viewer
#  Used In        : Python
#  Used As        : Practice
#  Problem      =>
#                   Given input JSON file we parse the and seprate the json with the level_2 nesting 
#  Thoughts     => 
#                   We are using the JSON library for the processing the input.After we process the initial
#                   key then we separate the nested JSON key values into the dictionary format via childOfparent
#                   function which output the separate the data in JSON. 
"""

import json
def childOfparent(parent, **data):
    for key in keysOfjson:
        temp = {}
        if type(keysOfjson.get(key)) in (dict, list):
            temp[key] = keysOfjson.get(key)
            with open(parent + "_" + key + ".json", 'w') as f:
                f.write(json.dumps(temp, sort_keys=True, indent=4, separators=(',', ': ')))
        parent = key


data = json.loads(open('input').read())
root = []
keysOfjson = {}
for i in data:
    root.append(i)
parent = root.pop()
parent = parent
for criteria in data[parent]:
    temp = {}
    for key, value in criteria.items():
        if type(value) in (int, float, bool, str):
            temp[key] = value
        else:
            keysOfjson[key] = value
    with open(parent + ".json", 'w') as f:
        f.write(json.dumps(temp, sort_keys=True, indent=4, separators=(',', ': ')))
    childOfparent(parent, **keysOfjson)
