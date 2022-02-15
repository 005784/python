import json

person_dict = {"name": "pranee",
"languages": ["English", "telugu"],
"age": 22
}

with open('person.json', 'w') as json_file:
  json.dump(person_dict, json_file)

