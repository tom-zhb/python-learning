import json

filename = "name.json"
with open(filename) as  file_obj:
    numbers = json.load(file_obj)

print(numbers)