import json

person = {
    "name": "Dilwar",
    "age": 19,
    "city": "Mumbai"
}

with open("data.json","w") as f:
    json.dump(person,f)

with open("data.json","r") as f:
    print(   json.load(f))
