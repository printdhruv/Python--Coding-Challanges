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
