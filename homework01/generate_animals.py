import petname
import json
import random

data={}
heads=['snake', 'bull', 'lion', 'raven', 'bunny']

data['animals']=[]

for i in range(20):
	head=heads[random.randint(0,3)]
	body=petname.name()+"-"+petname.name()
	arms=random.randrange(2,11,2)
	legs=random.randrange(3,13,3)
	tails=arms+legs
	data['animals'].append({'head':head, 'body':body, 'arms':arms, 'legs':legs, 'tails':tails})

with open ('animals.json', 'w') as out:
	json.dump(data,out,indent=2)

	

