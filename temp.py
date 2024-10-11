import json

data: dict = {
    "id": 1,
    "is_auth": True,
    "some": "some 2",
    "tegs": ["ad", 'ab']
}

print("some 2" in list(data.keys()))


# data_json = json.dumps(data, indent=4)
# print(type(data_json))
# print(data_json)
#
# data_2 = json.loads(data_json)
# print(data_2)
#
# data = str(data)
# print(type(data))
