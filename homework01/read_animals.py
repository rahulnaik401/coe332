import json, random

with open('animals.json','r') as f:
	animals=json.load(f)

print(animals['animals'][random.randint(0,19)])
