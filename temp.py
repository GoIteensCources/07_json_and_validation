import json

data = {
    "id": 1,
    "is_auth": True,
    "tegs": ["ad", 'ab']
}


data_json = json.dumps(data, indent=4)
print(type(data_json))
print(data_json)

data_2 = json.loads(data_json)
print(data_2)
